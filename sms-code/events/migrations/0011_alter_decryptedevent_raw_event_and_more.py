# Generated by Django 5.0.3 on 2024-04-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_decryptedevent_raw_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decryptedevent',
            name='raw_event',
            field=models.IntegerField(default=-1, verbose_name='Raw Event'),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='raw_event',
            field=models.IntegerField(default=-1, verbose_name='Raw Event'),
        ),
    ]