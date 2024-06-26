import datetime as datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field



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
    ages_permis = (
        ('with_out', 'Без возрастных ограничений'),
        ('age1', '12+'),
        ('age2', '16+'),
        ('age3', '18+'),
    )
    club = None
    title = models.CharField(max_length=128, verbose_name='Название')
    admins = models.ManyToManyField(get_user_model(), related_name='clubsadmins')
    not_approved = models.ManyToManyField(get_user_model(), related_name='notapproved', null=True, blank=True)

    description = models.TextField(blank=True, null=True, verbose_name='Информация о клубе')
    # short_desc = models.TextField(blank=True, null=True, verbose_name='Доп.информация о клубе')
    short_desc = CKEditor5Field(blank=True, null=True, verbose_name="Доп.информация о клубе", config_name='extends')
    moderate = models.BooleanField(default=False, verbose_name='Модерировать')

    image = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None, null=True, blank=True,
                             verbose_name='Изображение')
    tg = models.CharField(max_length=256, null=True, blank=True, verbose_name='Телеграм')
    cat = models.CharField(max_length=64, choices=cats, verbose_name='Направления', null=True)
    age = models.CharField(max_length=32, choices=ages_permis, verbose_name='Возрастные ограничения', null=True, blank=True, default='with_out')

    class Meta:
        verbose_name_plural = 'Клубы'


class ModelPost(BaseModel):
    type_content_choices = [
        ('news', 'Новости'),
        ('article', 'Статьи'),
    ]

    text = CKEditor5Field(blank=True, null=True, verbose_name="Текст", config_name='extends')
    image = models.FileField(upload_to='uploads/posts/', default=None, null=True, blank=True,
                             verbose_name='Изображение')
    datetime = models.DateField(blank=True, null=True, default=datetime.date.today)
    type_content = models.CharField(max_length=32, choices=type_content_choices, verbose_name='Тип поста', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Посты'
        ordering = ['-datetime']


class EventModel(BaseModel):
    slug = None
    description = RichTextField(blank=True, null=True, verbose_name="Описание события")
    format = models.CharField(max_length=16, choices=BaseModel.format_choices, verbose_name="Формат проведения")


    class Meta:
        verbose_name_plural = 'События'


class Notifs(models.Model):
    club = models.ForeignKey("Club", on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True)
    sender = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Отправитель')
    receiver = models.ManyToManyField(get_user_model(), related_name='notifs_receiver', null=True, blank=False, verbose_name='Получатель')
    timestamp = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время')

    class Meta:
        verbose_name_plural = 'Сообщения'



