from django.db import models

from accounts.models import Account, AccountUser
from configurations.models import AlarmCode, Device


class RawEvent(models.Model):
    data = models.TextField()
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class DecryptedEvent(models.Model):
    raw_event = models.ForeignKey(RawEvent, on_delete=models.CASCADE)
    alarm_code = models.ForeignKey(AlarmCode, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    zone = models.IntegerField(default=0)
    user = models.ForeignKey(AccountUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)