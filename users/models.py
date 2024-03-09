from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fio = models.CharField(max_length=64, verbose_name='ФИО', null=True)
    clubs = models.ManyToManyField("app_clubs.Club", related_name='members_clubs')
    image = models.FileField(upload_to='uploads/users/%Y/%m/%d/', default=None, null=True, blank=True, verbose_name='Изображение')
