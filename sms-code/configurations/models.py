from django.utils.translation import gettext as _
from django.core.cache import cache
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator 

from accounts.models import Account

#from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .utils import get_ports


class AlarmCode(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'code',], name='configurations.alarmcode.unique_id')
        ]
    
        verbose_name = _("Alarm Code")
        verbose_name_plural = _("Alarm Codes")
    
    ALARM_TYPES = (
        (0, _("None")),
        (1, _("Auto Log")),
        (2, _("Auto Test")),
        #(3, _("Gaurd Round")),
        (4, _("Opening")),
        (5, _("Closing")),
    )
        
    DECRYPTION_TYPES= (
        (0, _("Zone")),
        (1, _("User"))
    )
    
    partition = models.IntegerField(default=0, db_index=True, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name=_("Partition"))

    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True, verbose_name=_("Account"))
    code = models.CharField(max_length=16, db_index=True, validators=[RegexValidator(regex=r"^[ER](\d+)$", message=_('Code does not comply'),)], verbose_name=_("Code"))
    description = models.CharField(max_length=40, verbose_name=_("Description"))
    
    #0 Zone, 1 User
    decryption_type = models.IntegerField(default=0, choices=DECRYPTION_TYPES, verbose_name=_("Decryption Type"))

    # TYPE
    alarm_type = models.IntegerField(default=0, choices=ALARM_TYPES, verbose_name=_("Alarm Type"))

    return_delay = models.IntegerField(default=0, verbose_name=_("Delay"))

    is_periodic = models.BooleanField(default=False, verbose_name=_("Scheduled"))
    periodic_interval_minutes = models.IntegerField(default=0, verbose_name=_("Minutes"))
    periodic_interval_hours = models.IntegerField(default=0, verbose_name=_("Hours"))
    
    #priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(9)])
    #delay = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    
    def __str__(self):
            return self.description 


class Device(models.Model):

    class Meta:
        verbose_name = _("Device")
        verbose_name_plural = _("Devices")
        
        
    BAUD_RATES = (
        (9600 , "9600"),
        (11440 , "11440"),
        (19200 , "19200"),
        (115200 , "115200"),  
    )
    
    TYPES = (
        ("mcdi", "MCDI"),
        ("surgard", "SurGard")
    )
    
    END_LINES = (
        ("<CR>", "<CR>"), 
        ("<DC4>", "<DC4>")
    )
    
    name = models.CharField(max_length=30, unique=True, verbose_name=_("Name"))
    type = models.CharField(max_length=10, choices=TYPES, verbose_name=_("Type"))

    com = models.CharField(max_length=30, unique=True, choices=get_ports, verbose_name=_("COM"))
    baud_rate = models.IntegerField(default=9600, choices=BAUD_RATES, verbose_name=_("Baud Rate"))

    end_line = models.CharField(max_length=10, choices=END_LINES, verbose_name=_("End Line"))

    def __str__(self):
            return self.name
        

@receiver(post_save, sender=Device)
def restart_scheduler(sender, instance, created, **kwargs):
    cache.set("devices:kill-device:" + instance.name, "true", timeout=None)


# @receiver(pre_delete, sender=Device)
# def delete_device_task(sender, instance, using, **kwargs):
#     instance.task.delete()
# 
# @receiver(pre_save, sender=Device)
# def create_device_task(sender, instance, **kwargs):
#     if not instance.id:
# 
#         schedule, created2 = IntervalSchedule.objects.get_or_create(
#             every=10,
#             period=IntervalSchedule.SECONDS,
#         )
#         instance.task = PeriodicTask.objects.create(
#             interval=schedule,
#             name=instance.name,
#             task="events.tasks.message_listener",
#             args=json.dumps([
#                 instance.id, instance.com, instance.baud_rate,
#                 instance.end_line, instance.decryption_configurations
#             ]),
#             kwargs=json.dumps({
#                 
#             })
#         )
#         
# @receiver(post_save, sender=Device)
# def update_device_task(sender, instance, created, **kwargs):
#     if not created:
#         schedule, created2 = IntervalSchedule.objects.get_or_create(
#             every=10,
#             period=IntervalSchedule.SECONDS,
#         )
#         instance.task.interval = schedule
#         instance.task.name = instance.name
#         instance.task.task = "events.tasks.message_listener"
#         args=json.dumps([
#             instance.id, instance.com, instance.baud_rate,
#             instance.end_line, instance.decryption_configurations
#         ]),
#         kwargs=json.dumps({
#             
#         })
#         instance.task.save()