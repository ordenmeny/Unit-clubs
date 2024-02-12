from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    format_choices = [
        ("Онлайн", "Онлайн"),
        ("Офлайн", "Офлайн"),
    ]

    title = models.CharField(max_length=64, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, db_index=True, null=False, blank=True, unique=True)
    club = models.ForeignKey("Club", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Club(BaseModel):
    club = None
    description = models.TextField(blank=True, null=True, verbose_name='Информация о клубе')


    class Meta:
        verbose_name_plural = 'Клубы'


class ModelPost(BaseModel):
    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    class Meta:
        verbose_name_plural = 'Посты'


class EventModel(BaseModel):
    description = models.TextField(blank=True, null=True, verbose_name="Описание события")
    format = models.CharField(max_length=16, choices=BaseModel.format_choices, verbose_name="Формат проведения")

    class Meta:
        verbose_name_plural = 'События'
