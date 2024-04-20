# Generated by Django 5.0.3 on 2024-04-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_decryptedevent_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decryptedevent',
            name='custom',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='line_no',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='protocole',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='decryptedevent',
            name='receiveer_no',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='custom',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='line_no',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='protocole',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='historicaldecryptedevent',
            name='receiveer_no',
            field=models.IntegerField(default=-1),
        ),
    ]