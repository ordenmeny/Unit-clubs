# Generated by Django 4.2.9 on 2024-03-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0020_club_cat_club_tg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='cat',
            field=models.CharField(choices=[('sport', 'СПОРТ'), ('it', 'IT'), ('cybersport', 'КИБЕРСПОРТ'), ('literature', 'ЛИТЕРАТУРА'), ('culture', 'КУЛЬТУРА'), ('chatting', 'ОБЩЕНИЕ'), ('painting', 'РИСОВАНИЕ'), ('music', 'МУЗЫКА'), ('handwork', 'РУКОДЕЛИЕ'), ('another', 'ДРУГОЕ')], max_length=64, null=True, verbose_name='Направления'),
        ),
    ]
