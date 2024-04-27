import datetime
from django.db import models

from django.utils.translation import gettext as _
from django.conf import settings

from accounts.models import Account
from simple_history.models import HistoricalRecords


class ServiceOrder(models.Model):
    
    class Meta:
        verbose_name = _("Service Order")
        verbose_name_plural = _("Service Orders")

    STATUS_CHOICES = (
        (0,_("Created")),
        (1,_("Under Review")),
        (2,_("Under Processing")),
        (3,_("Done")),
        (-1,_("Canceled"))
    )
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_("Account"))
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, db_index=True, verbose_name=_("Status"))
    
    summary = models.CharField(max_length=120, verbose_name=_("Summary"))
    
    request = models.TextField(verbose_name=_("Request"))
    
    internal_notes = models.TextField(blank=True, verbose_name=_("Internal Notes"))
    
    response = models.TextField(blank=True, verbose_name=_("Response"))
    
    # Accounts Control
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    closed_at = models.DateTimeField(blank=True, null=True, verbose_name=_("Closed At"))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Created By"))
    
    history = HistoricalRecords(verbose_name=_("Service Order History"))

    def save(self, *args, **kwargs):
        
        old_instance = ServiceOrder.objects.filter(pk=self.id).first()
        
        if old_instance:
            if (self.status == 3 or self.status == -1) and (old_instance.status != 0 or old_instance.status != 1 or old_instance.status != 2):
                self.closed_at = datetime.datetime.now()
        else:
            if self.status == 3 or self.status == -1:
                self.closed_at = datetime.datetime.now()

        if self.status == 0 or self.status == 1 or self.status == 2:
            self.closed_at = None
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.summary + " - " + self.account.name