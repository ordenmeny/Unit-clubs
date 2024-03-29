from django.forms import ModelForm
from app_clubs.models import *
from django import forms


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ('title', 'description', 'tg', 'cat', 'moderate', 'image')


class FormJoinClub(forms.Form):
    pass


class FormPost(ModelForm):
    class Meta:
        model = ModelPost
        fields = ['title', 'text', 'image', 'type_content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'size': '40'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'type_content': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }


class FormEvent(ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'description', 'format']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'format': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }


class FormNotifs(ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Notifs
        fields = ['text']
