# Generated by Django 4.2.9 on 2024-02-19 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_clubs', '0004_remove_eventmodel_moderate_remove_modelpost_moderate'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='not_approved',
            field=models.ManyToManyField(related_name='notapproved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='club',
            name='admins',
            field=models.ManyToManyField(related_name='clubsadmins', to=settings.AUTH_USER_MODEL),
        ),
    ]