# Generated by Django 5.0.3 on 2024-04-26 19:43

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_copy_alarm_codes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalaccount',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'التدقيق', 'verbose_name_plural': 'historical الحسابات'},
        ),
        migrations.AlterField(
            model_name='account',
            name='fire_dept_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثاتي'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name0',
            field=models.CharField(default='Default', max_length=30, verbose_name='القسم الإفتراضي'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name1',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الأول'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name10',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم العاشر'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name2',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الثاني'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name3',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الثالث'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name4',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الرابع'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name5',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الخامس'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name6',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم السادس'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name7',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم السابع'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name8',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الثامن'),
        ),
        migrations.AlterField(
            model_name='account',
            name='partition_name9',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم التاسع'),
        ),
        migrations.AlterField(
            model_name='account',
            name='receiver_phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='ؤقم المستقبل'),
        ),
        migrations.AlterField(
            model_name='account',
            name='transmitter_phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='ؤقم المرسل'),
        ),
        migrations.AlterField(
            model_name='account',
            name='whatsapp_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الواتساب'),
        ),
        migrations.AlterField(
            model_name='account',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='الرمز البريدي'),
        ),
        migrations.AlterField(
            model_name='accountnote',
            name='note',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='ملاحظه'),
        ),
        migrations.AlterField(
            model_name='accountnote',
            name='timer',
            field=models.BooleanField(db_index=True, default=False, verbose_name='موقت'),
        ),
        migrations.AlterField(
            model_name='accountnote',
            name='timer_interval_hours',
            field=models.IntegerField(default=0, verbose_name='ساعة'),
        ),
        migrations.AlterField(
            model_name='accountnote',
            name='timer_interval_minutes',
            field=models.IntegerField(default=0, verbose_name='دقيقة'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='fire_dept_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثاتي'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name0',
            field=models.CharField(default='Default', max_length=30, verbose_name='القسم الإفتراضي'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name1',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الأول'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name10',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم العاشر'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name2',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الثاني'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name3',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الثالث'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name4',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الرابع'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name5',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الخامس'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name6',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم السادس'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name7',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم السابع'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name8',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم الثامن'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='partition_name9',
            field=models.CharField(blank=True, max_length=30, verbose_name='القسم التاسع'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='receiver_phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='ؤقم المستقبل'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='transmitter_phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='ؤقم المرسل'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='whatsapp_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الواتساب'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='الرمز البريدي'),
        ),
    ]