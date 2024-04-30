# Generated by Django 5.0.3 on 2024-04-30 06:02

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'المدينة',
                'verbose_name_plural': 'المدن',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'المجموعة',
                'verbose_name_plural': 'المجموعات',
            },
        ),
        migrations.CreateModel(
            name='InstallationCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='اسم الشركة')),
                ('phone_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الأول')),
                ('phone_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الثاني')),
            ],
            options={
                'verbose_name': 'شركة التركيب',
                'verbose_name_plural': 'شركات التركيب',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='معرف الحساب')),
                ('name', models.CharField(max_length=40, verbose_name='اسم الحساب')),
                ('address_line1', models.CharField(blank=True, max_length=30, verbose_name='العنوات الأول')),
                ('address_line2', models.CharField(blank=True, max_length=30, verbose_name='العنوات الثاتي')),
                ('address_line3', models.CharField(blank=True, max_length=30, verbose_name='العنوان الثالث')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='الرمز البريدي')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='البريد الإلكتروني')),
                ('phone_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الأول')),
                ('phone_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الثاني')),
                ('whatsapp_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الواتساب')),
                ('security_number', models.CharField(blank=True, max_length=20, verbose_name='رقم الحرس')),
                ('memo', models.TextField(blank=True, max_length=120, verbose_name='ملاحظة')),
                ('police_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الأول')),
                ('police_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثاتي')),
                ('police_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثالث')),
                ('fire_dept_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الأول')),
                ('fire_dept_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثاتي')),
                ('fire_dept_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثالث')),
                ('emergency_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الأول')),
                ('emergency_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثاتي')),
                ('emergency_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثالث')),
                ('partition_name0', models.CharField(default='Default', max_length=30, verbose_name='القسم الإفتراضي')),
                ('partition_name1', models.CharField(blank=True, max_length=30, verbose_name='القسم الأول')),
                ('partition_name2', models.CharField(blank=True, max_length=30, verbose_name='القسم الثاني')),
                ('partition_name3', models.CharField(blank=True, max_length=30, verbose_name='القسم الثالث')),
                ('partition_name4', models.CharField(blank=True, max_length=30, verbose_name='القسم الرابع')),
                ('partition_name5', models.CharField(blank=True, max_length=30, verbose_name='القسم الخامس')),
                ('partition_name6', models.CharField(blank=True, max_length=30, verbose_name='القسم السادس')),
                ('partition_name7', models.CharField(blank=True, max_length=30, verbose_name='القسم السابع')),
                ('partition_name8', models.CharField(blank=True, max_length=30, verbose_name='القسم الثامن')),
                ('partition_name9', models.CharField(blank=True, max_length=30, verbose_name='القسم التاسع')),
                ('partition_name10', models.CharField(blank=True, max_length=30, verbose_name='القسم العاشر')),
                ('copy_alarm_codes', models.BooleanField(default=False, verbose_name='Copy Alarm Codes')),
                ('installation_date', models.DateField(blank=True, null=True, verbose_name='تاريخ التركيب')),
                ('installation_note', models.TextField(blank=True, max_length=120, verbose_name='ملاحظة التركيب')),
                ('receiver_phone_number', models.CharField(blank=True, max_length=20, verbose_name='رقم المستقبل')),
                ('transmitter_phone_number', models.CharField(blank=True, max_length=20, verbose_name='رقم المرسل')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='حدّث عند')),
                ('copy_alarm_codes_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account', verbose_name='Copy Alarm Codes From')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.city', verbose_name='المدينة')),
                ('groups', models.ManyToManyField(blank=True, related_name='accounts', to='accounts.group', verbose_name='المجموعات')),
                ('installation_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.installationcompany', verbose_name='شركة التركيب')),
            ],
            options={
                'verbose_name': 'الحساب',
                'verbose_name_plural': 'الحسابات',
            },
        ),
        migrations.CreateModel(
            name='AccountNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decrypted_event', models.PositiveBigIntegerField(default=-1, verbose_name='الحدث المترجم')),
                ('note', models.TextField(blank=True, max_length=120, null=True, verbose_name='ملاحظه')),
                ('timer', models.BooleanField(db_index=True, default=False, verbose_name='مؤقت')),
                ('timer_interval_minutes', models.IntegerField(default=0, verbose_name='دقيقة')),
                ('timer_interval_hours', models.IntegerField(default=0, verbose_name='ساعة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='حدّث عند')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الحساب')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من')),
            ],
            options={
                'verbose_name': 'Account Note',
                'verbose_name_plural': 'Account Notes',
            },
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partition', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='القسم')),
                ('name', models.CharField(max_length=40, verbose_name='الإسم')),
                ('code', models.IntegerField(verbose_name='الرمز')),
                ('in_out_codes', models.CharField(blank=True, max_length=20, verbose_name='In-Out Codes')),
                ('password', models.CharField(blank=True, max_length=15, verbose_name='كلمة المرور')),
                ('phone_number1', models.CharField(blank=True, max_length=20, verbose_name='الرقم الأول')),
                ('phone_number2', models.CharField(blank=True, max_length=20, verbose_name='الرقم الثاني')),
                ('phone_number3', models.CharField(blank=True, max_length=20, verbose_name='الرقم الثالث')),
                ('title1', models.CharField(blank=True, max_length=150, verbose_name='التعريف')),
                ('title2', models.CharField(blank=True, max_length=150, verbose_name='التعريف')),
                ('title3', models.CharField(blank=True, max_length=150, verbose_name='التعريف')),
                ('holiday_begins', models.DateField(blank=True, null=True, verbose_name='بداية العطلة')),
                ('holiday_ends', models.DateField(blank=True, null=True, verbose_name='نهاية العطلة')),
                ('keypad_code', models.CharField(blank=True, max_length=6, verbose_name='Keypad Code')),
                ('hot_user', models.BooleanField(default=False, verbose_name='Hot User')),
                ('authorized_days_sat', models.BooleanField(default=False, verbose_name='السبت')),
                ('authorized_days_sun', models.BooleanField(default=False, verbose_name='الأحد')),
                ('authorized_days_mon', models.BooleanField(default=False, verbose_name='الاثنين')),
                ('authorized_days_tue', models.BooleanField(default=False, verbose_name='الثلاثاء')),
                ('authorized_days_wed', models.BooleanField(default=False, verbose_name='الأربعاء')),
                ('authorized_days_thu', models.BooleanField(default=False, verbose_name='الخميس')),
                ('authorized_days_fri', models.BooleanField(default=False, verbose_name='الجمعة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='حدّث عند')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الحساب')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من')),
            ],
            options={
                'verbose_name': 'المستهلك',
                'verbose_name_plural': 'المستهلكين',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.PositiveIntegerField(db_index=True, verbose_name='معرف الحساب')),
                ('name', models.CharField(max_length=40, verbose_name='اسم الحساب')),
                ('address_line1', models.CharField(blank=True, max_length=30, verbose_name='العنوات الأول')),
                ('address_line2', models.CharField(blank=True, max_length=30, verbose_name='العنوات الثاتي')),
                ('address_line3', models.CharField(blank=True, max_length=30, verbose_name='العنوان الثالث')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='الرمز البريدي')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='البريد الإلكتروني')),
                ('phone_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الأول')),
                ('phone_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='الرقم الثاني')),
                ('whatsapp_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الواتساب')),
                ('security_number', models.CharField(blank=True, max_length=20, verbose_name='رقم الحرس')),
                ('memo', models.TextField(blank=True, max_length=120, verbose_name='ملاحظة')),
                ('police_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الأول')),
                ('police_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثاتي')),
                ('police_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الشرطة الثالث')),
                ('fire_dept_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الأول')),
                ('fire_dept_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثاتي')),
                ('fire_dept_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الإطفاء الثالث')),
                ('emergency_number1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الأول')),
                ('emergency_number2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثاتي')),
                ('emergency_number3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region='SY', verbose_name='رقم الطوارئ الثالث')),
                ('partition_name0', models.CharField(default='Default', max_length=30, verbose_name='القسم الإفتراضي')),
                ('partition_name1', models.CharField(blank=True, max_length=30, verbose_name='القسم الأول')),
                ('partition_name2', models.CharField(blank=True, max_length=30, verbose_name='القسم الثاني')),
                ('partition_name3', models.CharField(blank=True, max_length=30, verbose_name='القسم الثالث')),
                ('partition_name4', models.CharField(blank=True, max_length=30, verbose_name='القسم الرابع')),
                ('partition_name5', models.CharField(blank=True, max_length=30, verbose_name='القسم الخامس')),
                ('partition_name6', models.CharField(blank=True, max_length=30, verbose_name='القسم السادس')),
                ('partition_name7', models.CharField(blank=True, max_length=30, verbose_name='القسم السابع')),
                ('partition_name8', models.CharField(blank=True, max_length=30, verbose_name='القسم الثامن')),
                ('partition_name9', models.CharField(blank=True, max_length=30, verbose_name='القسم التاسع')),
                ('partition_name10', models.CharField(blank=True, max_length=30, verbose_name='القسم العاشر')),
                ('copy_alarm_codes', models.BooleanField(default=False, verbose_name='Copy Alarm Codes')),
                ('installation_date', models.DateField(blank=True, null=True, verbose_name='تاريخ التركيب')),
                ('installation_note', models.TextField(blank=True, max_length=120, verbose_name='ملاحظة التركيب')),
                ('receiver_phone_number', models.CharField(blank=True, max_length=20, verbose_name='رقم المستقبل')),
                ('transmitter_phone_number', models.CharField(blank=True, max_length=20, verbose_name='رقم المرسل')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='أنشئ عند')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='حدّث عند')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('city', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.city', verbose_name='المدينة')),
                ('copy_alarm_codes_from', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.account', verbose_name='Copy Alarm Codes From')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='أنشئ من')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('installation_company', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.installationcompany', verbose_name='شركة التركيب')),
            ],
            options={
                'verbose_name': 'التدقيق',
                'verbose_name_plural': 'historical الحسابات',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partition', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='القسم')),
                ('name', models.CharField(max_length=30, verbose_name='الإسم')),
                ('code', models.IntegerField(verbose_name='الرمز')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الحساب')),
            ],
            options={
                'verbose_name': 'المنطقة',
                'verbose_name_plural': 'المناطق',
            },
        ),
        migrations.AddConstraint(
            model_name='accountuser',
            constraint=models.UniqueConstraint(fields=('account', 'partition', 'code'), name='accounts.accountuser.unique_id'),
        ),
        migrations.AddConstraint(
            model_name='zone',
            constraint=models.UniqueConstraint(fields=('account', 'partition', 'code'), name='accounts.zone.unique_id'),
        ),
    ]
