# Generated by Django 5.0.7 on 2024-11-04 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bethistory',
            name='bet_amount',
        ),
    ]