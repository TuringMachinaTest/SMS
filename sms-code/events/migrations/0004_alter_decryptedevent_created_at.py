# Generated by Django 5.0.3 on 2024-03-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_decryptedevent_commit_decryptedevent_follow_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decryptedevent',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]