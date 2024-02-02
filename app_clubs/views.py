from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView, TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .utils import DataMixin


class CreateClub(DataMixin, CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'app_clubs/create_club.html'
    item_selected = 'create_club'

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_club')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class JoinClub(UpdateView):
    model = Club
    form_class = FormJoinClub
    slug_url_kwarg = 'club_slug'
    template_name = 'app_clubs/join_club.html'

    def get_success_url(self):
        return reverse_lazy('app_clubs:join_club', kwargs={'club_slug': self.kwargs['club_slug']})

    def form_valid(self, form):
        # Во время валидации формы(без полей):

        # получаем объект клуба по слагу из url
        club = Club.objects.get(slug=self.kwargs['club_slug'])

        # получаем объект user
        user = get_user_model().objects.get(username=self.request.user)

        # Добавляем в объекте клуба в поле members объект пользователя
        club.members.add(user)

        return super().form_valid(form)


class ListClubs(DataMixin, ListView):
    context_object_name = 'clubs'
    model = Club
    template_name = 'app_clubs/list_clubs.html'
    item_selected = 'list_clubs'


class CreatePost(DataMixin, CreateView):
    model = ModelPost
    form_class = FormPost
    template_name = 'app_clubs/create_post.html'
    item_selected = 'create_post'

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_post')

    def form_valid(self, form):
        form.instance.title = slugify(form.instance.title)
        return super().form_valid(form)


class CreateEvent(DataMixin, CreateView):
    model = EventModel
    form_class = FormEvent
    template_name = 'app_clubs/create_event.html'
    item_selected = 'create_event'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_event')


class HomePage(TemplateView):
    template_name = 'app_clubs/index.html'
