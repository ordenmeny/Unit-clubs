from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import UserForm, LoginForm
from django.contrib import messages


class LoginUser(LoginView):
    template_name = 'users/login.html'
    item_selected = 'login'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('app_clubs:profile_user')


class SignUp(CreateView):
    form_class = UserForm
    template_name = 'users/signup.html'
    item_selected = 'signup'

    def get_success_url(self):
        return reverse_lazy('users:login')


class UpdateProfile(UpdateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'users/signup.html'
    # slug_url_kwarg = 'post_slug'

    def get_success_url(self):
        messages.success(self.request, 'Профиль изменен')
        return reverse_lazy('app_clubs:profile_user')

