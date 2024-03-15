# Generated by Django 4.2.9 on 2024-03-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0019_notifs'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='cat',
            field=models.CharField(choices=[('СПОРТ', 'СПОРТ'), ('IT', 'IT'), ('КИБЕРСПОРТ', 'КИБЕРСПОРТ'), ('ЛИТЕРАТУРА', 'ЛИТЕРАТУРА'), ('КУЛЬТУРА', 'КУЛЬТУРА'), ('ОБЩЕНИЕ', 'ОБЩЕНИЕ'), ('РИСОВАНИЕ', 'РИСОВАНИЕ'), ('МУЗЫКА', 'МУЗЫКА'), ('РУКОДЕЛИЕ', 'РУКОДЕЛИЕ'), ('ДРУГОЕ', 'ДРУГОЕ')], max_length=64, null=True, verbose_name='Направления'),
        ),
        migrations.AddField(
            model_name='club',
            name='tg',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Телеграм'),
        ),
    ]