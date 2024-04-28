from datetime import datetime
from django.db import models

from accounts.models import Account, AccountNote, AccountUser, Zone
from configurations.models import AlarmCode, Device, Schedule
from simple_history.models import HistoricalRecords

from django.conf import settings

from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel
from django.utils.translation import gettext as _


class RawEvent(PostgresPartitionedModel):
    class Meta:
        ordering = ('-id',)

        verbose_name = _("Raw Event")
        verbose_name_plural = _("Raw Events")
        
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["created_at"]
    
    data = models.TextField()
    device = models.ForeignKey(Device, on_delete=models.PROTECT, verbose_name=_("Device"))
    
    decrypted = models.BooleanField(default=False, db_index=True, verbose_name=_("Decrypted"))
    has_errors = models.BooleanField(default=False, db_index=True, verbose_name=_("Has Errors"))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    
    def __str__(self):
            return self.data 

class DecryptedEvent(PostgresPartitionedModel):
    class Meta:
        ordering = ('-id',)

        verbose_name = _("Decrypted Event")
        verbose_name_plural = _("Decrypted Events")

    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["created_at"]
        
    STATUS_CHOICES = (
        (-1, _("locked")),
        (0, _("Not Saved")),
        (1, _("Saved")),
        (2, _("Pending")),
        (3, _("Follow")),
        (4, _("Delayed Return")),
        (5, _("Delayed Periodic"))
    )
    
    raw_event = models.IntegerField(default=-1, verbose_name=_("Raw Event"))
    
    protocole = models.IntegerField(default=-1, verbose_name=_("Protocole"))
    receiveer_no = models.IntegerField(default=-1, verbose_name=_("Receiveer No"))
    line_no = models.IntegerField(default=-1, verbose_name=_("Line No"))
    
    alarm_code = models.ForeignKey(AlarmCode, on_delete=models.PROTECT, db_index=True, null=True, blank=True, verbose_name=_("Alarm Code"))
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True, db_index=True, verbose_name=_("Account"))
    partition = models.IntegerField(default=0, db_index=True, verbose_name=_("Partition"))
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, null=True, blank=True,db_index=True, verbose_name=_("Zone"))
    user = models.ForeignKey(AccountUser, on_delete=models.PROTECT, null=True, blank=True, db_index=True, verbose_name=_("User"))
    
    success = models.BooleanField(default=True, db_index=True, verbose_name=_("Success"))
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, db_index=True, verbose_name=_("Status"))
    
    custom = models.BooleanField(default=True, verbose_name=_("Custom"))
   
    note = models.TextField(max_length=120, null=True, blank=True, verbose_name=_("Note"))
        
    timer = models.BooleanField(default=False, db_index=True, verbose_name=_("Timer"))
    timer_interval_minnutes = models.IntegerField(default=0, verbose_name=_("Minutes"))
    timer_interval_hours = models.IntegerField(default=0, verbose_name=_("Hours"))

    account_note = models.TextField(max_length=120, null=True, blank=True, verbose_name=_("Account Note"))
    account_note_timer = models.BooleanField(default=False, verbose_name=_("Timer"))
    note_timer_interval_minnutes = models.IntegerField(default=0, verbose_name=_("Minutes"))
    note_timer_interval_hours = models.IntegerField(default=0, verbose_name=_("Hours"))
    
    has_return = models.BooleanField(default=False, db_index=True, verbose_name=_("Has Return"))
    delayed_return = models.BooleanField(default=False, db_index=True, verbose_name=_("Delayed Return"))
    handled_return_delay = models.BooleanField(default=False, db_index=True, verbose_name=_("Handled Return Delay"))

    is_last_periodic_event = models.BooleanField(default=False, db_index=True, verbose_name=_("Is Last Periodic Event"))
    delayed_periodic = models.BooleanField(default=False, db_index=True, verbose_name=_("Delayed Periodic"))
    handled_periodic_delay = models.BooleanField(default=False, db_index=True, verbose_name=_("Handled Periodic Delay"))

    is_out_of_schedule = models.BooleanField(default=False, db_index=True, verbose_name=_("Is Out Of Schedule"))
    
    created_at = models.DateTimeField(verbose_name=_("Created At"))
    locked_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Locked At"))
    locked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, db_index=True, verbose_name=_("Locked By"))
    
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_("Updated At"))
    
    history = HistoricalRecords(verbose_name=_("History"))

    def save(self, *args, **kwargs):
        if self.status != -1:
            self.locked_at = None
            
        if self.account_note != "":
            account_note = AccountNote(
                account=self.account, 
                note=self.account_note, 
                note_timer=self.account_note_timer, 
                note_timer_interval_minnutes=self.note_timer_interval_minnutes, 
                note_timer_interval_hours=self.note_timer_interval_hours
            )
            account_note.save()
            
        if self._state.adding is True and self.alarm_code and self.account and self.partition and self.alarm_code.code[0] == "R":
            related_code = self.alarm_code.code.replace("R", "E")
            related_alarm_code = AlarmCode.objects.filter(account=self.account, partition=self.partition, code=related_code).first()
            if related_alarm_code:
                related_event = DecryptedEvent.objects.filter(has_return=False, account=self.account, partition=self.partition, alarm_code=related_alarm_code).first()
                if related_event:
                    related_event.has_return = True
                    related_event.save()
                    self.has_return = True
                    
        if self._state.adding is True and self.alarm_code and self.alarm_code.is_periodic and self.partition:
            last_periodic_event = DecryptedEvent.objects.filter(account=self.account, partition=self.partition, alarm_code=self.alarm_code, is_last_periodic_event=True).first()
            if last_periodic_event:
                last_periodic_event.is_last_periodic_event = False
                last_periodic_event.save()
        
        # Opening Time
        if self._state.adding is True and self.alarm_code and self.alarm_code.alarm_type == 4 and self.partition:
            schedule = Schedule.objects.filter(account=self.account, partition=self.partition).first()
            if schedule:
                day_of_the_week = self.created_at.weekday()
                if not schedule.get_is_open(day_of_the_week):
                    self.is_out_of_schedule = True
                else:
                    opening_time_from, opening_time_to = schedule.get_opening_time(day_of_the_week)
                    if opening_time_from and opening_time_to:
                        if self.created_at.time() < opening_time_from and self.created_at.time() > opening_time_to:
                            self.is_out_of_schedule = True
        
        # Closing Time
        if self._state.adding is True and self.alarm_code and self.alarm_code.alarm_type == 5 and self.partition:
            schedule = Schedule.objects.filter(account=self.account, partition=self.partition).first()
            if schedule:
                day_of_the_week = self.created_at.weekday()
                if not schedule.get_is_open(day_of_the_week):
                    self.is_out_of_schedule = True
                else:
                    closing_time_from, closing_time_to = schedule.get_closing_time(day_of_the_week)
                    if closing_time_from and closing_time_to:
                        if self.created_at.time() < closing_time_from and self.created_at.time() > closing_time_to:
                            self.is_out_of_schedule = True
                                    
        super().save(*args, **kwargs)