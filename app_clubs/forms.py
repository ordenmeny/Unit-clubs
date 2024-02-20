from django.forms import ModelForm
from app_clubs.models import *
from django import forms


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ('title', 'description')


class FormJoinClub(forms.Form):
    pass


class FormPost(ModelForm):
    class Meta:
        model = ModelPost
        fields = ['title', 'text']


class FormEvent(ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'description', 'format']
