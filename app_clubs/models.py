from django.contrib.auth import get_user_model
from django.db import models


class Club(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, db_index=True, null=False, blank=True, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Информация о клубе')
    members = models.ManyToManyField(get_user_model(), related_name='club_members', blank=True)

    def __str__(self):
        return self.title


class ModelPost(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, db_index=True, null=False, blank=True, unique=True)
    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    def __str__(self):
        return self.title


class EventModel(models.Model):
    format_choices = [
        ("Онлайн", "Онлайн"),
        ("Офлайн", "Офлайн"),
    ]
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, db_index=True, null=False, blank=True, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Описание события")
    format = models.CharField(max_length=16, choices=format_choices, verbose_name="Формат проведения")


    def __str__(self):
        return self.title
