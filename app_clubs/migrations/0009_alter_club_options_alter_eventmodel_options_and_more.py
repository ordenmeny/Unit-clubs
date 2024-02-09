# Generated by Django 4.2.9 on 2024-02-09 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0008_modelpost_club_alter_club_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'verbose_name_plural': 'Клубы'},
        ),
        migrations.AlterModelOptions(
            name='eventmodel',
            options={'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='modelpost',
            options={'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_clubs.club'),
        ),
        migrations.AlterField(
            model_name='modelpost',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Заголовок'),
        ),
    ]
