# Generated by Django 5.0.3 on 2024-03-18 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmcode',
            name='name',
        ),
        migrations.AddField(
            model_name='alarmcode',
            name='delay',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AddField(
            model_name='alarmcode',
            name='description',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alarmcode',
            name='priority',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='alarmcode',
            name='code',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Code does not comply', regex='^[ER](\\d+)$')]),
        ),
    ]