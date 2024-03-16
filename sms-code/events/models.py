from django.db import models

from accounts.models import Account, AccountUser, Zone
from configurations.models import AlarmCode, Device
from simple_history.models import HistoricalRecords

class RawEvent(models.Model):
    class Meta:
        ordering = ('-id',)
    
    data = models.TextField()
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    
    decrypted = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return self.data 

class DecryptedEvent(models.Model):
    class Meta:
        ordering = ('-id',)
    
    STATUS_CHOICES = (
        (-1,"locked"),
        (0,"Not Saved"),
        (1,"Saved"),
        (2,"Pending"),
        (3, "Follow")
    )
    
    raw_event = models.ForeignKey(RawEvent, on_delete=models.CASCADE)
    receiveer_no = models.IntegerField()
    line_no = models.IntegerField()
    
    alarm_code = models.ForeignKey(AlarmCode, on_delete=models.PROTECT, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True)
    partition = models.IntegerField(default=0)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(AccountUser, on_delete=models.PROTECT, null=True, blank=True)
    
    success = models.BooleanField(default=False)
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
    custom = models.BooleanField(default=False)
   
    note = models.TextField(max_length=120, null=True, blank=True)
   
    created_at = models.DateTimeField()
    locked_at = models.DateTimeField(null=True, blank=True)
    
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if self.status != -1:
            self.locked_at = None
            
        super().save(*args, **kwargs)
