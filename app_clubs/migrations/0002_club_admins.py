# Generated by Django 4.2.9 on 2024-02-18 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='admins',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
