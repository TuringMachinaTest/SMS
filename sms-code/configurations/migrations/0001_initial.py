# Generated by Django 5.0.3 on 2024-03-17 22:05

import configurations.utils
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('type', models.CharField(choices=[('mcdi', 'MCDI'), ('surgard', 'SurGard')], max_length=10)),
                ('com', models.CharField(choices=configurations.utils.get_ports, max_length=30, unique=True)),
                ('baud_rate', models.IntegerField(choices=[(9600, '9600'), (11440, '11440'), (19200, '19200'), (115200, '115200')], default=9600)),
                ('end_line', models.CharField(choices=[('<CR>', '<CR>'), ('<DC4>', '<DC4>')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(message='Code does not comply', regex='^[ER](\\d+)$')])),
                ('name', models.CharField(max_length=30)),
                ('type', models.IntegerField(choices=[(0, 'Zone'), (1, 'User')], default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
        migrations.AddConstraint(
            model_name='alarmcode',
            constraint=models.UniqueConstraint(fields=('account', 'code'), name='configurations.alarmcode.unique_id'),
        ),
    ]
