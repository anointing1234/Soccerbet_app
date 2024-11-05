# Generated by Django 5.0.7 on 2024-11-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_bethistory_bet_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bethistory',
            name='bet_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
