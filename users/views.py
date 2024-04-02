from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as auth_login


class LoginUser(LoginView):
    template_name = 'users/login.html'
    item_selected = 'login'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('app_clubs:profile_user')


class SignUp(CreateView):
    # После авторизации перенапрявлять на страницу профиль пользователя для

    form_class = UserForm
    template_name = 'users/signup.html'
    item_selected = 'signup'

    extra_context = {'height': '100%'}

    def get_success_url(self):
        return reverse_lazy('users:login')

    def form_valid(self, form):
        auth_login(self.request, form.save())
        messages.success(self.request, 'Вы зарегистрировались')
        return HttpResponseRedirect(reverse_lazy('app_clubs:profile_user'))


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'users/signup.html'
    extra_context = {'type_btn': 'Сохранить', 'height': '600px'}

    def get_success_url(self):
        messages.success(self.request, 'Профиль изменен')
        return reverse_lazy('app_clubs:profile_user')
