# Generated by Django 5.0.3 on 2024-03-14 23:56

import configurations.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='com',
            field=models.CharField(choices=configurations.utils.get_ports, max_length=30, unique=True),
        ),
    ]
