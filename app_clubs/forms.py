from django.forms import ModelForm

from app_clubs.models import Club


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ('title', 'description')


class FormJoinClub(ModelForm):
    class Meta:
        model = Club
        fields = []
