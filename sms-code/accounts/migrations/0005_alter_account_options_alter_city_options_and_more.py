# Generated by Django 5.0.3 on 2024-04-21 13:24

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_options_alter_accountuser_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'الحساب', 'verbose_name_plural': 'الحسابات'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'المدينة', 'verbose_name_plural': 'المدن'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'المجموعة', 'verbose_name_plural': 'المجموعات'},
        ),
        migrations.AlterModelOptions(
            name='historicalaccount',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'تاريخ', 'verbose_name_plural': 'historical الحسابات'},
        ),
        migrations.AlterModelOptions(
            name='installationcompany',
            options={'verbose_name': 'شركة التركيب', 'verbose_name_plural': 'شركات التركيب'},
        ),
        migrations.AlterField(
            model_name='account',
            name='address_line1',
            field=models.CharField(blank=True, max_length=30, verbose_name='العنوات الأول'),
        ),
        migrations.AlterField(
            model_name='account',
            name='address_line2',
            field=models.CharField(blank=True, max_length=30, verbose_name='العنوات الثاتي'),
        ),
        migrations.AlterField(
            model_name='account',
            name='address_line3',
            field=models.CharField(blank=True, max_length=30, verbose_name='العنوان الثالث'),
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.city', verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=30, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='account',
            name='emergency_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الأول'),
        ),
        migrations.AlterField(
            model_name='account',
            name='emergency_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثاتي'),
        ),
        migrations.AlterField(
            model_name='account',
            name='emergency_number3',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثالث'),
        ),
        migrations.AlterField(
            model_name='account',
            name='fire_dept_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الأول'),
        ),
        migrations.AlterField(
            model_name='account',
            name='fire_dept_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='ؤقم الإطفاء الثاتي'),
        ),
        migrations.AlterField(
            model_name='account',
            name='fire_dept_number3',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثالث'),
        ),
        migrations.AlterField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='accounts', to='accounts.group', verbose_name='المجموعات'),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='معؤف الحساب'),
        ),
        migrations.AlterField(
            model_name='account',
            name='installation_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.installationcompany', verbose_name='شركة التركيب'),
        ),
        migrations.AlterField(
            model_name='account',
            name='installation_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ التركيب'),
        ),
        migrations.AlterField(
            model_name='account',
            name='installation_note',
            field=models.TextField(blank=True, max_length=120, verbose_name='ملاحظة التركيب'),
        ),
        migrations.AlterField(
            model_name='account',
            name='memo',
            field=models.TextField(blank=True, max_length=120, verbose_name='ملاحظة'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=40, verbose_name='اسم الحساب'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الأول'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الثاني'),
        ),
        migrations.AlterField(
            model_name='account',
            name='police_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الأول'),
        ),
        migrations.AlterField(
            model_name='account',
            name='police_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثاتي'),
        ),
        migrations.AlterField(
            model_name='account',
            name='police_number3',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثالث'),
        ),
        migrations.AlterField(
            model_name='account',
            name='security_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='رقم الحرس'),
        ),
        migrations.AlterField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='حدّث عند'),
        ),
        migrations.AlterField(
            model_name='account',
            name='whatsapp_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='ؤقم الواتساب'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الحساب'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_fri',
            field=models.BooleanField(default=False, verbose_name='الجمعة'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_mon',
            field=models.BooleanField(default=False, verbose_name='الاثنين'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_sat',
            field=models.BooleanField(default=False, verbose_name='السبت'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_sun',
            field=models.BooleanField(default=False, verbose_name='الأحد'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_thu',
            field=models.BooleanField(default=False, verbose_name='الخميس'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_tue',
            field=models.BooleanField(default=False, verbose_name='الثلاثاء'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='authorized_days_wed',
            field=models.BooleanField(default=False, verbose_name='الأربعاء'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='phone_number1',
            field=models.CharField(blank=True, max_length=20, verbose_name='الرقم الأول'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=20, verbose_name='الرقم الثاني'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='حدّث عند'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='address_line1',
            field=models.CharField(blank=True, max_length=30, verbose_name='العنوات الأول'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='address_line2',
            field=models.CharField(blank=True, max_length=30, verbose_name='العنوات الثاتي'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='address_line3',
            field=models.CharField(blank=True, max_length=30, verbose_name='العنوان الثالث'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='city',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.city', verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='created_at',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='أنشئ عند'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='email',
            field=models.EmailField(blank=True, max_length=30, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='emergency_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الأول'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='emergency_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثاتي'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='emergency_number3',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثالث'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='fire_dept_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الأول'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='fire_dept_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='ؤقم الإطفاء الثاتي'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='fire_dept_number3',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثالث'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='id',
            field=models.IntegerField(db_index=True, verbose_name='معؤف الحساب'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='installation_company',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.installationcompany', verbose_name='شركة التركيب'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='installation_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ التركيب'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='installation_note',
            field=models.TextField(blank=True, max_length=120, verbose_name='ملاحظة التركيب'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='memo',
            field=models.TextField(blank=True, max_length=120, verbose_name='ملاحظة'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='name',
            field=models.CharField(max_length=40, verbose_name='اسم الحساب'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='phone_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الأول'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='phone_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الثاني'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='police_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الأول'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='police_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثاتي'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='police_number3',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثالث'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='security_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='رقم الحرس'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='updated_at',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='حدّث عند'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='whatsapp_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='ؤقم الواتساب'),
        ),
        migrations.AlterField(
            model_name='installationcompany',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='اسم الشركة'),
        ),
        migrations.AlterField(
            model_name='installationcompany',
            name='phone_number1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الأول'),
        ),
        migrations.AlterField(
            model_name='installationcompany',
            name='phone_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الثاني'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الحساب'),
        ),
        migrations.CreateModel(
            name='AccountNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, max_length=120, null=True, verbose_name='Note')),
                ('note_timer', models.BooleanField(default=False, verbose_name='Note Timer')),
                ('note_timer_interval_minnutes', models.IntegerField(default=0, verbose_name='Minutes')),
                ('note_timer_interval_hours', models.IntegerField(default=0, verbose_name='Hours')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='حدّث عند')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من')),
            ],
            options={
                'verbose_name': 'Account Note',
                'verbose_name_plural': 'Account Notes',
            },
        ),
    ]