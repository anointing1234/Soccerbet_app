# Generated by Django 5.0.7 on 2024-11-04 14:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_bethistory_bet_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premierleaguegame',
            name='date',
        ),
        migrations.RemoveField(
            model_name='premierleaguegame',
            name='time',
        ),
        migrations.AddField(
            model_name='premierleaguegame',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]