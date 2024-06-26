# Generated by Django 4.2.9 on 2024-04-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clubs', '0040_alter_club_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='age',
            field=models.CharField(blank=True, choices=[('with_out', 'Без возрастных ограничений'), ('age1', '12+'), ('age1', '16+'), ('age1', '18+')], default='with_out', max_length=32, null=True, verbose_name='Возрастные ограничения'),
        ),
    ]
