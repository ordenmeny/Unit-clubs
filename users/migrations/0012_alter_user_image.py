# Generated by Django 4.2.9 on 2024-04-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_image_alter_user_tg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, default='uploads/users/user_no_photo.jpg', null=True, upload_to='uploads/users/%Y/%m/%d/', verbose_name='Аватарка'),
        ),
    ]