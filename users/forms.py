from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.forms import ModelForm
from django import forms


class UserForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control block-opacity input-height',
                                      'placeholder': 'Имя пользователя'}))
    fio = forms.CharField(label='ФИО',
                          widget=forms.TextInput(
                              attrs={'class': 'form-control block-opacity input-height', 'placeholder': 'ФИО'}))
    tg = forms.CharField(label='Телеграм',
                         widget=forms.TextInput(
                             attrs={'class': 'form-control block-opacity input-height', 'placeholder': 'Телеграм'}))
    desc = forms.CharField(label='Описание',
                           widget=forms.Textarea(
                               attrs={'class': 'form-control block-opacity input-height', 'placeholder': 'Описание'}))

    image = forms.FileField(label='Картинка',
                            widget=forms.FileInput(
                                attrs={'class': 'form-control input-file-opacity', 'placeholder': 'Картинка'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control block-opacity input-height',
                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control block-opacity input-height',
                                                                  'placeholder': 'Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'fio', 'tg', 'desc', 'password1', 'password2', 'image']


class CustomUserChangeForm(UserChangeForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control block-opacity input-height',
                                      'placeholder': 'Имя пользователя'}))
    fio = forms.CharField(label='ФИО',
                          widget=forms.TextInput(
                              attrs={'class': 'form-control block-opacity input-height', 'placeholder': 'ФИО'}))
    tg = forms.CharField(label='Телеграм',
                         widget=forms.TextInput(
                             attrs={'class': 'form-control block-opacity input-height', 'placeholder': 'Телеграм'}))
    desc = forms.CharField(label='Описание',
                           widget=forms.Textarea(
                               attrs={'class': 'form-control block-opacity input-height', 'placeholder': 'Описание'}))
    image = forms.FileField(label='Картинка',
                            widget=forms.FileInput(
                                attrs={'class': 'form-control input-file-opacity', 'placeholder': 'Картинка'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'fio', 'tg', 'desc', 'image']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control block-opacity input-height',
                                      'placeholder': 'Имя пользователя'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class': 'form-control block-opacity input-height',
                   'placeholder': 'Пароль'}
        ),
    )
