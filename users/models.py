from django.contrib.auth.models import AbstractUser
from django.db import models
from app_clubs.models import Club


class User(AbstractUser):
    clubs = models.ManyToManyField(Club, blank=True, null=True, related_name='members_clubs')