# Generated by Django 4.2.9 on 2024-03-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0010_rename_file_image_club_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='moderate',
            field=models.BooleanField(default=False, verbose_name='Модерировать'),
        ),
    ]
