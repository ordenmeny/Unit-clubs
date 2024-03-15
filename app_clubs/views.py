from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .utils import DataMixin, RequiredClubMember
from django.contrib.auth.mixins import LoginRequiredMixin
from pytils.translit import slugify


class ProfileUser(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'app_clubs/profile_user.html'
    item_selected = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_clubs'] = self.request.user.clubs.all()

        return context


class ProfileClub(RequiredClubMember, TemplateView):
    template_name = 'app_clubs/profile_club.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_club'] = self.request.current_club
        context['events'] = EventModel.objects.filter(club=self.request.current_club)
        context['posts'] = ModelPost.objects.filter(club=self.request.current_club)
        context['members'] = get_user_model().objects.filter(clubs=self.request.current_club)
        return context


class CreateClub(LoginRequiredMixin, DataMixin, CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'app_clubs/create_club.html'
    item_selected = 'create_club'

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_club')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        self.object = form.save()
        self.object.admins.add(self.request.user)
        self.request.user.clubs.add(self.object)
        return super().form_valid(form)


class ListClubs(LoginRequiredMixin, DataMixin, ListView):
    context_object_name = 'clubs'
    model = Club
    template_name = 'app_clubs/list_clubs.html'
    item_selected = 'list_clubs'

    def get_queryset(self):
        if self.kwargs['cat'] == 'all':
            return Club.objects.all()
        return Club.objects.filter(cat=self.kwargs['cat'])


class CreatePost(RequiredClubMember, DataMixin, CreateView):
    model = ModelPost
    form_class = FormPost
    template_name = 'app_clubs/create_post.html'
    for_admin = True
    item_selected = 'create_post'

    def get_success_url(self):
        return reverse_lazy('app_clubs:home_page')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.club = Club.objects.get(slug=self.kwargs['club_slug'])

        return super().form_valid(form)


class JoinClub(LoginRequiredMixin, FormView):
    template_name = 'app_clubs/join_club.html'
    form_class = FormJoinClub
    success_url = reverse_lazy('app_clubs:home_page')

    def form_valid(self, form):
        current_user = self.request.user
        current_club = Club.objects.get(slug=self.kwargs['club_slug'])

        if not current_club.moderate:
            # Если не нужно модерировать
            current_user.clubs.add(current_club)
            return super().form_valid(form)
        else:
            # Если нужно модерировать
            current_club.not_approved.add(current_user)
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = Club.objects.get(slug=self.kwargs['club_slug'])

        return context

    def get_success_url(self):
        return reverse_lazy('app_clubs:profile_club', kwargs={'club_slug': self.kwargs['club_slug']})


class ApproveMembers(RequiredClubMember, FormView, ListView):
    form_class = FormJoinClub
    template_name = 'app_clubs/not_approve_members.html'
    context_object_name = 'not_approved_members'
    success_url = reverse_lazy('app_clubs:home_page')
    for_admin = True

    def form_valid(self, form):
        user_id = self.request.POST['user_id']
        user_to_approve = get_user_model().objects.get(pk=user_id)

        current_club = Club.objects.get(slug=self.kwargs["club_slug"])

        current_club.not_approved.remove(user_to_approve)
        user_to_approve.clubs.add(current_club)

        return super().form_valid(form)

    def get_queryset(self):
        current_club = Club.objects.get(slug=self.kwargs['club_slug'])
        not_approved_members = current_club.not_approved.all()
        return not_approved_members

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_club = Club.objects.get(slug=self.kwargs['club_slug'])
        context['current_club'] = current_club.slug
        return context


class CreateEvent(RequiredClubMember, DataMixin, CreateView):
    model = EventModel
    form_class = FormEvent
    template_name = 'app_clubs/create_event.html'
    for_admin = True

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        current_club = Club.objects.get(slug=self.kwargs['club_slug'])
        form.instance.club = current_club
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_event', kwargs={'club_slug': self.kwargs['club_slug']})


class HomePage(TemplateView):
    template_name = 'app_clubs/index.html'
    extra_context = {'cats': cats}


class ShowContent(ListView):
    template_name = 'app_clubs/show_content.html'

    def get_queryset(self):
        if self.kwargs['content'] == 'events':
            return EventModel.objects.all()
        if self.kwargs['content'] == 'posts':
            return ModelPost.objects.all()


