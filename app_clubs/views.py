from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
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


    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        # return {'item_selected': 'text for check'}

    def get_success_url(self):
        return reverse_lazy('app_clubs:create_club')


class JoinClub(UpdateView):
    model = Club
    form_class = FormJoinClub
    slug_url_kwarg = 'club_slug'
    template_name = 'app_clubs/join_club.html'

    def get_success_url(self):
        return reverse_lazy('app_clubs:join_club', kwargs={'club_slug': self.kwargs['club_slug']})

    def form_valid(self, form):
        club = Club.objects.get(slug=self.kwargs['club_slug'])
        user = get_user_model().objects.get(username=self.request.user)

        club.members.add(user)

        return super().form_valid(form)


class ListClubs(DataMixin, ListView):
    context_object_name = 'clubs'
    model = Club
    template_name = 'app_clubs/list_clubs.html'
    item_selected = 'list_clubs'
