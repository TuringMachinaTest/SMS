from django.db import models

from accounts.models import Account, AccountUser
from configurations.models import Device, ContactIdCode


# Create your models here.
class RawEvent(models.Model):
    data = models.TextField()
    device_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class DecryptedEvent(models.Model):
    raw_event = models.ForeignKey(RawEvent, on_delete=models.CASCADE)
    contact_id_code = models.ForeignKey(ContactIdCode, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    zone = models.IntegerField(default=0)
    user = models.ForeignKey(AccountUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

