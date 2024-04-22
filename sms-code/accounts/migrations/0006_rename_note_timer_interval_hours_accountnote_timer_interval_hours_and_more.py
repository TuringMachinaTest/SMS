# Generated by Django 5.0.3 on 2024-04-22 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_options_alter_city_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountnote',
            old_name='note_timer_interval_hours',
            new_name='timer_interval_hours',
        ),
        migrations.RenameField(
            model_name='accountnote',
            old_name='note_timer_interval_minnutes',
            new_name='timer_interval_minnutes',
        ),
        migrations.RemoveField(
            model_name='accountnote',
            name='note_timer',
        ),
        migrations.AddField(
            model_name='accountnote',
            name='account',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الحساب'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountnote',
            name='timer',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Timer'),
        ),
    ]