# Generated by Django 4.2.9 on 2024-03-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0012_alter_club_not_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpost',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='uploads/posts/'),
        ),
    ]
