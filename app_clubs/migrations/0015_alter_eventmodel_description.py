# Generated by Django 4.2.9 on 2024-03-09 14:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0014_alter_club_title_alter_eventmodel_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
