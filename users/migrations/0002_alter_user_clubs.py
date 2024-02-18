# Generated by Django 4.2.9 on 2024-02-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='clubs',
            field=models.ManyToManyField(related_name='members_clubs', to='app_clubs.club'),
        ),
    ]
