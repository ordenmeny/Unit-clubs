from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import ModelForm
from django import forms


class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control block-opacity input-height', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class': 'form-control block-opacity input-height', 'placeholder': 'Пароль'}
        ),
    )
