# Generated by Django 4.2.9 on 2024-03-09 15:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0015_alter_eventmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание события'),
        ),
    ]