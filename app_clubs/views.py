from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, FormView, DetailView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .utils import DataMixin, RequiredClubMember
from django.contrib.auth.mixins import LoginRequiredMixin
from pytils.translit import slugify
from django.contrib import messages


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
        messages.success(self.request, 'Клуб успешно создан')
        return reverse_lazy('app_clubs:list_clubs', kwargs={'cat': 'all'})

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
        messages.success(self.request, 'Пост создан')
        return reverse_lazy('app_clubs:profile_club', kwargs={'club_slug': self.kwargs['club_slug']})

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title[:40] + f'{self.request.current_club}')
        form.instance.club = self.request.current_club
        form.instance.author = self.request.user

        return super().form_valid(form)


class JoinClub(LoginRequiredMixin, FormView):
    template_name = 'app_clubs/join_club.html'
    form_class = FormJoinClub

    def form_valid(self, form):
        current_user = self.request.user
        current_club = Club.objects.get(slug=self.kwargs['club_slug'])

        if not current_club.moderate:
            # Если не нужно модерировать
            current_user.clubs.add(current_club)
            return super().form_valid(form)
        else:
            # Если нужно модерировать
            # Просходит добавление пользователя в раздел not_approved
            current_club.not_approved.add(current_user)
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = Club.objects.get(slug=self.kwargs['club_slug'])

        return context

    def get_success_url(self):
        messages.success(self.request, 'Вы были добавлены в клуб')
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

        current_club = self.request.current_club

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
        current_club = self.request.current_club
        form.instance.club = current_club
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Событие создано')
        return reverse_lazy('app_clubs:profile_club', kwargs={'club_slug': self.kwargs['club_slug']})


class HomePage(TemplateView):
    template_name = 'app_clubs/index.html'
    extra_context = {'cats': cats}


class ShowContent(RequiredClubMember, ListView):
    extra_context = {'param': 'None'}
    template_name = 'app_clubs/show_content.html'

    def dispatch(self, request, *args, **kwargs):
        content_type = self.kwargs['content']
        if content_type not in ('events', 'posts', 'members'):
            return redirect(reverse_lazy('app_clubs:page_error', kwargs={'type_error': '404'}))

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        content_type = self.kwargs['content']
        self.extra_context['content_type'] = content_type
        self.extra_context['current_club'] = self.request.current_club
        self.context_object_name = content_type

        if content_type == 'events':
            self.model = EventModel
            return EventModel.objects.filter(club=self.request.current_club)

        if content_type == 'posts':
            self.model = ModelPost
            return ModelPost.objects.filter(club=self.request.current_club)

        if content_type == 'members':
            self.model = get_user_model()
            return get_user_model().objects.filter(clubs=self.request.current_club)


class DetailPost(RequiredClubMember, DetailView):
    model = ModelPost
    template_name = 'app_clubs/detail_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = self.request.current_club

        return context


class PageError(TemplateView):
    template_name = 'app_clubs/page_error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        error = self.kwargs['type_error']
        if error == '404':
            context['text_error'] = 'Страница не найдена'
        if self.kwargs['type_error'] == '403':
            context['text_error'] = 'Доступ запрещен'

        return context


class DeletePost(RequiredClubMember, DeleteView):
    model = ModelPost
    template_name = 'app_clubs/delete_post.html'
    slug_url_kwarg = 'post_slug'
    for_admin = True

    def get_success_url(self):
        messages.success(self.request, 'Пост удален')
        return reverse_lazy('app_clubs:profile_club', kwargs={'club_slug': self.kwargs['club_slug']})


class UpdatePost(RequiredClubMember, UpdateView):
    model = ModelPost
    form_class = FormPost
    # fields = ['title', 'text', 'image', 'type_content']
    template_name = 'app_clubs/create_post.html'
    slug_url_kwarg = 'post_slug'

    def get_success_url(self):
        messages.success(self.request, 'Пост изменен')
        return reverse_lazy('app_clubs:profile_club', kwargs={'club_slug': self.kwargs['club_slug']})
