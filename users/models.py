from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    clubs = models.ManyToManyField("app_clubs.Club", related_name='members_clubs')
