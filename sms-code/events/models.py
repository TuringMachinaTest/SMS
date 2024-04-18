from django.db import models

from accounts.models import Account, AccountUser, Zone
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
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    
    decrypted = models.BooleanField(default=False, db_index=True)
    has_errors = models.BooleanField(default=False, db_index=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
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
    
    raw_event = models.IntegerField()
    
    protocole = models.IntegerField(default=-1)
    receiveer_no = models.IntegerField(default=-1)
    line_no = models.IntegerField(default=-1)
    
    alarm_code = models.ForeignKey(AlarmCode, on_delete=models.PROTECT, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True, db_index=True,)
    partition = models.IntegerField(default=0, db_index=True)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, null=True, blank=True,db_index=True)
    user = models.ForeignKey(AccountUser, on_delete=models.PROTECT, null=True, blank=True, db_index=True)
    
    success = models.BooleanField(default=False, db_index=True)
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, db_index=True)
    
    custom = models.BooleanField(default=True)
   
    note = models.TextField(max_length=120, null=True, blank=True)
   
    created_at = models.DateTimeField()
    locked_at = models.DateTimeField(null=True, blank=True)
    locked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)
    
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if self.status != -1:
            self.locked_at = None
                        
        super().save(*args, **kwargs)