# Generated by Django 4.2.9 on 2024-02-19 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0003_club_moderate_eventmodel_moderate_modelpost_moderate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='moderate',
        ),
        migrations.RemoveField(
            model_name='modelpost',
            name='moderate',
        ),
    ]