# Generated by Django 5.0.3 on 2024-03-13 10:09

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_partition_name0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='partition',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
