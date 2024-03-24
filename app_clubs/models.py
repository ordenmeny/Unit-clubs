from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

cats = [
    ("sport", "СПОРТ"),
    ("it", "IT"),
    ("cybersport", "КИБЕРСПОРТ"),
    ("literature", "ЛИТЕРАТУРА"),
    ("culture", "КУЛЬТУРА"),
    ("chatting", "ОБЩЕНИЕ"),
    ("painting", "РИСОВАНИЕ"),
    ("music", "МУЗЫКА"),
    ("handwork", "РУКОДЕЛИЕ"),
    ("another", "ДРУГОЕ"),
]


class BaseModel(models.Model):
    format_choices = [
        ("Онлайн", "Онлайн"),
        ("Офлайн", "Офлайн"),
    ]

    title = models.CharField(max_length=128, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, db_index=True, null=False, blank=True, unique=True)
    club = models.ForeignKey("Club", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Club(BaseModel):
    club = None
    admins = models.ManyToManyField(get_user_model(), related_name='clubsadmins')
    not_approved = models.ManyToManyField(get_user_model(), related_name='notapproved', null=True, blank=True)

    description = models.TextField(blank=True, null=True, verbose_name='Информация о клубе')
    moderate = models.BooleanField(default=False, verbose_name='Модерировать')

    image = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None, null=True, blank=True,
                             verbose_name='Изображение')
    tg = models.CharField(max_length=256, null=True, blank=True, verbose_name='Телеграм')
    cat = models.CharField(max_length=64, choices=cats, verbose_name='Направления', null=True)

    class Meta:
        verbose_name_plural = 'Клубы'


class ModelPost(BaseModel):
    # text = models.TextField(blank=True, null=True, verbose_name='Текст')
    text = RichTextField(blank=True, null=True, verbose_name="Текст")
    image = models.FileField(upload_to='uploads/posts/', default=None, null=True, blank=True,
                             verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Посты'


class EventModel(BaseModel):
    # description = models.TextField(blank=True, null=True, verbose_name="Описание события")
    description = RichTextField(blank=True, null=True, verbose_name="Описание события")
    format = models.CharField(max_length=16, choices=BaseModel.format_choices, verbose_name="Формат проведения")

    class Meta:
        verbose_name_plural = 'События'


class Notifs(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
