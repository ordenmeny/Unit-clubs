from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm


class LoginUser(LoginView):
    template_name = 'users/login.html'
    item_selected = 'login'

    def get_success_url(self):
        return reverse_lazy('users:login')


class SignUp(CreateView):
    form_class = UserForm
    template_name = 'users/signup.html'
    item_selected = 'signup'

    def get_success_url(self):
        return reverse_lazy('users:login')
