# Generated by Django 4.2.9 on 2024-03-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0022_alter_modelpost_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpost',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
