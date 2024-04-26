# Generated by Django 5.0.3 on 2024-04-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_decryptedevent_delayed_periodic_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldecryptedevent',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'التدقيق', 'verbose_name_plural': 'historical Decrypted Events'},
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='account_note_timer',
            field=models.BooleanField(default=False, verbose_name='موقت'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='note',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='ملاحظه'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='note_timer_interval_hours',
            field=models.IntegerField(default=0, verbose_name='ساعة'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='note_timer_interval_minnutes',
            field=models.IntegerField(default=0, verbose_name='دقيقة'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='success',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Success'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='timer',
            field=models.BooleanField(db_index=True, default=False, verbose_name='موقت'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='timer_interval_hours',
            field=models.IntegerField(default=0, verbose_name='ساعة'),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='timer_interval_minnutes',
            field=models.IntegerField(default=0, verbose_name='دقيقة'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='account_note_timer',
            field=models.BooleanField(default=False, verbose_name='موقت'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='note',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='ملاحظه'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='note_timer_interval_hours',
            field=models.IntegerField(default=0, verbose_name='ساعة'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='note_timer_interval_minnutes',
            field=models.IntegerField(default=0, verbose_name='دقيقة'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='success',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Success'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='timer',
            field=models.BooleanField(db_index=True, default=False, verbose_name='موقت'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='timer_interval_hours',
            field=models.IntegerField(default=0, verbose_name='ساعة'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='timer_interval_minnutes',
            field=models.IntegerField(default=0, verbose_name='دقيقة'),
        ),
    ]