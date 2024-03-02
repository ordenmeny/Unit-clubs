from django.shortcuts import render
from django.utils.text import slugify
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .utils import DataMixin, RequiredClubMember
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateClub(LoginRequiredMixin, DataMixin, CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'app_clubs/create_club.html'
    item_selected = 'create_club'

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_club')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class ListClubs(LoginRequiredMixin, DataMixin, ListView):
    context_object_name = 'clubs'
    model = Club
    template_name = 'app_clubs/list_clubs.html'
    item_selected = 'list_clubs'


class CreatePost(RequiredClubMember, DataMixin, CreateView):
    model = ModelPost
    form_class = FormPost
    template_name = 'app_clubs/create_post.html'
    for_admin = True

    def get_success_url(self):
        return reverse_lazy('app_clubs:home_page')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.club = Club.objects.get(slug=self.kwargs['club_slug'])
        return super().form_valid(form)


# class JoinClub(LoginRequiredMixin, View):
#     template_name = 'app_clubs/join_post.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current_club'] = Club.objects.get(slug=self.kwargs.get('club_slug'))
#         return context
#
#     # Пользователь выбирает клуб, переходит на подтверждающую страницу, нажимает кнопку.
#     # Если клуб не медерируется-просто добавляем в клуб(*)
#     # Если клуб модерируется:
#     # 1) добавялется в not_approved.
#     # 2) На странице админа выводится список из not_approved
#     # 3) Админ нажмимает на кнопку, пользователь добавляется в клуб(* то же действие)
#     #
#
#     def post(self, request, *args, **kwargs):
#         to_moderate = self.kwargs.get('club_slug')
#         # status = request.POST.get('status')  # параметр из формы
#
#         current_club = Club.objects.get(slug=self.kwargs.get('club_slug'))
#         current_user = request.user
#
#         if to_moderate == False:
#             # если не нужно модерировать-просто добавляем в БД
#             current_user.clubs.add(current_club)
#         # Если нужно модерировать:
#         if to_moderate:
#             current_club.not_approved.add(current_user)

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

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_event')


class HomePage(ListView):
    context_object_name = 'clubs'
    template_name = 'app_clubs/index.html'


    def get_queryset(self):
        if self.request.user.is_authenticated:
            my_clubs = self.request.user.clubs.all()
            return my_clubs
