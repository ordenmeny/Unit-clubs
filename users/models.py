from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fio = models.CharField(max_length=64, verbose_name='ФИО', null=True, blank=False)
    clubs = models.ManyToManyField("app_clubs.Club", related_name='members_clubs')
    image = models.FileField(upload_to='uploads/users/%Y/%m/%d/', default=None, null=True, blank=True, verbose_name='Аватарка')
    tg = models.CharField(max_length=128, verbose_name="Имя пользователя в телеграм", null=True, blank=True)
    desc = models.TextField(null=True, verbose_name='Описание о себе', blank=True)