# Generated by Django 4.2.9 on 2024-03-08 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0009_alter_club_file_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='file_image',
            new_name='image',
        ),
    ]