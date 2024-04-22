from django.db import models

from accounts.models import Account, AccountNote, AccountUser, Zone
from configurations.models import AlarmCode, Device
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
        (-1,"locked"),
        (0,"Not Saved"),
        (1,"Saved"),
        (2,"Pending"),
        (3, "Follow")
    )
    
    raw_event = models.IntegerField(verbose_name=_("Raw Event"))
    
    protocole = models.IntegerField(default=-1, verbose_name=_("Protocole"))
    receiveer_no = models.IntegerField(default=-1, verbose_name=_("Receiveer No"))
    line_no = models.IntegerField(default=-1, verbose_name=_("Line No"))
    
    alarm_code = models.ForeignKey(AlarmCode, on_delete=models.PROTECT, null=True, blank=True, verbose_name=_("Alarm Code"))
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True, db_index=True, verbose_name=_("Account"))
    partition = models.IntegerField(default=0, db_index=True, verbose_name=_("Partition"))
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, null=True, blank=True,db_index=True, verbose_name=_("Zone"))
    user = models.ForeignKey(AccountUser, on_delete=models.PROTECT, null=True, blank=True, db_index=True, verbose_name=_("User"))
    
    success = models.BooleanField(default=False, db_index=True, verbose_name=_("Success"))
    
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
                        
        super().save(*args, **kwargs)