# Generated by Django 5.0.3 on 2024-03-21 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0004_alarmcode_partition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarmcode',
            old_name='type',
            new_name='decryption_type',
        ),
    ]