from django.db import models

from accounts.models import Account, AccountUser, Zone
from configurations.models import AlarmCode, Device

class RawEvent(models.Model):
    class Meta:
        ordering = ('-created_at',)
    
    data = models.TextField()
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    
    decrypted = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)


class DecryptedEvent(models.Model):
    class Meta:
        ordering = ('-created_at',)
    
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
    
    alarm_code = models.ForeignKey(AlarmCode, on_delete=models.PROTECT, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True)
    partition = models.IntegerField(default=0)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(AccountUser, on_delete=models.PROTECT, null=True)
    
    success = models.BooleanField(default=False)
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
    custom = models.BooleanField(default=False)
   
    created_at = models.DateTimeField()
    