from django.forms import ModelForm
from app_clubs.models import *
from django import forms


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ('title', 'description', 'moderate', 'image')


class FormJoinClub(forms.Form):
    pass


class FormPost(ModelForm):
    class Meta:
        model = ModelPost
        fields = ['title', 'text', 'image']


class FormEvent(ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'description', 'format']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'format': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }
