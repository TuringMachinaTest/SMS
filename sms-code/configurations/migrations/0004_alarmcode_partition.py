# Generated by Django 5.0.3 on 2024-03-21 12:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0003_remove_alarmcode_delay_remove_alarmcode_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarmcode',
            name='partition',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
