# Generated by Django 5.0.3 on 2024-04-30 12:11

import django.db.models.deletion
import psqlextra.backend.migrations.operations.add_default_partition
import psqlextra.backend.migrations.operations.create_partitioned_model
import psqlextra.manager.manager
import psqlextra.models.partitioned
import psqlextra.types
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('configurations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        psqlextra.backend.migrations.operations.create_partitioned_model.PostgresCreatePartitionedModel(
            name='DecryptedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_event', models.IntegerField(default=-1, verbose_name='الحدث المشفر')),
                ('protocole', models.IntegerField(default=-1, verbose_name='Protocole')),
                ('receiveer_no', models.IntegerField(default=-1, verbose_name='Receiveer No')),
                ('line_no', models.IntegerField(default=-1, verbose_name='Line No')),
                ('partition', models.IntegerField(db_index=True, default=0, verbose_name='القسم')),
                ('success', models.BooleanField(db_index=True, default=True, verbose_name='نجاح')),
                ('status', models.IntegerField(choices=[(-1, 'مقفول'), (0, 'غير معالج'), (1, 'تمت معالجته'), (2, 'معلق'), (3, 'تتم متابعته'), (4, 'تاخر حدث العودة'), (5, 'تأخر في الجدولة')], db_index=True, default=0, verbose_name='الحالة')),
                ('note', models.TextField(blank=True, max_length=120, null=True, verbose_name='ملاحظه')),
                ('timer', models.BooleanField(db_index=True, default=False, verbose_name='مؤقت')),
                ('timer_interval_minnutes', models.PositiveIntegerField(default=0, verbose_name='دقيقة')),
                ('timer_interval_hours', models.PositiveIntegerField(default=0, verbose_name='ساعة')),
                ('account_note', models.TextField(blank=True, max_length=120, null=True, verbose_name='Account Note')),
                ('account_note_timer', models.BooleanField(default=False, verbose_name='مؤقت')),
                ('note_timer_interval_minnutes', models.PositiveIntegerField(default=0, verbose_name='دقيقة')),
                ('note_timer_interval_hours', models.PositiveIntegerField(default=0, verbose_name='ساعة')),
                ('has_return', models.BooleanField(db_index=True, default=False, verbose_name='يوجد حدث عودة')),
                ('delayed_return', models.BooleanField(db_index=True, default=False, verbose_name='تاخر حدث العودة')),
                ('handled_return_delay', models.BooleanField(db_index=True, default=False, verbose_name='تم التحقق من تأخير عودة الحدث')),
                ('is_last_periodic_event', models.BooleanField(db_index=True, default=False, verbose_name='إخر حدث مجدول')),
                ('delayed_periodic', models.BooleanField(db_index=True, default=False, verbose_name='تأخر في الجدولة')),
                ('handled_periodic_delay', models.BooleanField(db_index=True, default=False, verbose_name='تم التحقق من تأخير الجدولة')),
                ('is_out_of_schedule', models.BooleanField(db_index=True, default=False, verbose_name='خارج أوقات الدوام الرسمي')),
                ('is_user_out_of_schedule', models.BooleanField(db_index=True, default=False, verbose_name='خارج أيام دوام المستهلك')),
                ('is_user_holiday', models.BooleanField(db_index=True, default=False, verbose_name='عطلة المستهلك')),
                ('handled_out_of_schedule', models.BooleanField(db_index=True, default=False, verbose_name='تم التحقق من خروج الحدث عن أوقات الدوام')),
                ('created_at', models.DateTimeField(verbose_name='أنشئ عند')),
                ('locked_at', models.DateTimeField(blank=True, null=True, verbose_name='تم قفله عند')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='حدّث عند')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.account', verbose_name='الحساب')),
                ('alarm_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='configurations.alarmcode', verbose_name='رمز الإنذار')),
                ('locked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تم قفله من قبل')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.accountuser', verbose_name='المستخدم')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.zone', verbose_name='المنطقة')),
            ],
            options={
                'verbose_name': 'الحدث المترجم',
                'verbose_name_plural': 'الأحداث المترجمة',
                'ordering': ('-id',),
            },
            partitioning_options={
                'method': psqlextra.types.PostgresPartitioningMethod['RANGE'],
                'key': ['created_at'],
            },
            bases=(psqlextra.models.partitioned.PostgresPartitionedModel,),
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
        psqlextra.backend.migrations.operations.add_default_partition.PostgresAddDefaultPartition(
            model_name='DecryptedEvent',
            name='default',
        ),
        migrations.CreateModel(
            name='HistoricalDecryptedEvent',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('raw_event', models.IntegerField(default=-1, verbose_name='الحدث المشفر')),
                ('protocole', models.IntegerField(default=-1, verbose_name='Protocole')),
                ('receiveer_no', models.IntegerField(default=-1, verbose_name='Receiveer No')),
                ('line_no', models.IntegerField(default=-1, verbose_name='Line No')),
                ('partition', models.IntegerField(db_index=True, default=0, verbose_name='القسم')),
                ('success', models.BooleanField(db_index=True, default=True, verbose_name='نجاح')),
                ('status', models.IntegerField(choices=[(-1, 'مقفول'), (0, 'غير معالج'), (1, 'تمت معالجته'), (2, 'معلق'), (3, 'تتم متابعته'), (4, 'تاخر حدث العودة'), (5, 'تأخر في الجدولة')], db_index=True, default=0, verbose_name='الحالة')),
                ('note', models.TextField(blank=True, max_length=120, null=True, verbose_name='ملاحظه')),
                ('timer', models.BooleanField(db_index=True, default=False, verbose_name='مؤقت')),
                ('timer_interval_minnutes', models.PositiveIntegerField(default=0, verbose_name='دقيقة')),
                ('timer_interval_hours', models.PositiveIntegerField(default=0, verbose_name='ساعة')),
                ('account_note', models.TextField(blank=True, max_length=120, null=True, verbose_name='Account Note')),
                ('account_note_timer', models.BooleanField(default=False, verbose_name='مؤقت')),
                ('note_timer_interval_minnutes', models.PositiveIntegerField(default=0, verbose_name='دقيقة')),
                ('note_timer_interval_hours', models.PositiveIntegerField(default=0, verbose_name='ساعة')),
                ('has_return', models.BooleanField(db_index=True, default=False, verbose_name='يوجد حدث عودة')),
                ('delayed_return', models.BooleanField(db_index=True, default=False, verbose_name='تاخر حدث العودة')),
                ('handled_return_delay', models.BooleanField(db_index=True, default=False, verbose_name='تم التحقق من تأخير عودة الحدث')),
                ('is_last_periodic_event', models.BooleanField(db_index=True, default=False, verbose_name='إخر حدث مجدول')),
                ('delayed_periodic', models.BooleanField(db_index=True, default=False, verbose_name='تأخر في الجدولة')),
                ('handled_periodic_delay', models.BooleanField(db_index=True, default=False, verbose_name='تم التحقق من تأخير الجدولة')),
                ('is_out_of_schedule', models.BooleanField(db_index=True, default=False, verbose_name='خارج أوقات الدوام الرسمي')),
                ('is_user_out_of_schedule', models.BooleanField(db_index=True, default=False, verbose_name='خارج أيام دوام المستهلك')),
                ('is_user_holiday', models.BooleanField(db_index=True, default=False, verbose_name='عطلة المستهلك')),
                ('handled_out_of_schedule', models.BooleanField(db_index=True, default=False, verbose_name='تم التحقق من خروج الحدث عن أوقات الدوام')),
                ('created_at', models.DateTimeField(verbose_name='أنشئ عند')),
                ('locked_at', models.DateTimeField(blank=True, null=True, verbose_name='تم قفله عند')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='حدّث عند')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.account', verbose_name='الحساب')),
                ('alarm_code', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='configurations.alarmcode', verbose_name='رمز الإنذار')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('locked_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='تم قفله من قبل')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.accountuser', verbose_name='المستخدم')),
                ('zone', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.zone', verbose_name='المنطقة')),
            ],
            options={
                'verbose_name': 'التدقيق',
                'verbose_name_plural': 'historical الأحداث المترجمة',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        psqlextra.backend.migrations.operations.create_partitioned_model.PostgresCreatePartitionedModel(
            name='RawEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('decrypted', models.BooleanField(db_index=True, default=False, verbose_name='مترجم')),
                ('has_errors', models.BooleanField(db_index=True, default=False, verbose_name='يوجد أخطاء')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='أنشئ عند')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configurations.device', verbose_name='الجهاز')),
            ],
            options={
                'verbose_name': 'الحدث المشفر',
                'verbose_name_plural': 'الأحداث المشفرة',
                'ordering': ('-id',),
            },
            partitioning_options={
                'method': psqlextra.types.PostgresPartitioningMethod['RANGE'],
                'key': ['created_at'],
            },
            bases=(psqlextra.models.partitioned.PostgresPartitionedModel,),
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
        psqlextra.backend.migrations.operations.add_default_partition.PostgresAddDefaultPartition(
            model_name='RawEvent',
            name='default',
        ),
    ]
