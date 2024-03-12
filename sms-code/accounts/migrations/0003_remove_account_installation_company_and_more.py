# Generated by Django 5.0.3 on 2024-03-12 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_installationcompany_account_installation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='installation_company',
        ),
        migrations.AddField(
            model_name='account',
            name='installation_company_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='installation_company_phone_number1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='installation_company_phone_number2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='partition',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.DeleteModel(
            name='InstallationCompany',
        ),
    ]
