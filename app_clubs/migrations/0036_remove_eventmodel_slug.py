# Generated by Django 4.2.9 on 2024-04-03 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0035_alter_club_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='slug',
        ),
    ]
