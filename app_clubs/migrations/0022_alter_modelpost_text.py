# Generated by Django 4.2.9 on 2024-03-24 09:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0021_alter_club_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelpost',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
