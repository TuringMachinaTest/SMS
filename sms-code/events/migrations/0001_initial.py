# Generated by Django 5.0.3 on 2024-03-14 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configurations.device')),
            ],
        ),
        migrations.CreateModel(
            name='DecryptedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account')),
                ('alarm_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurations.alarmcode')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.accountuser')),
                ('raw_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.rawevent')),
            ],
        ),
    ]
