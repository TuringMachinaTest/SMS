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
    
    TYPES= (
        (0, "Zone"),
        (1, "User")
    )
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    code = models.CharField(max_length=16, validators=[RegexValidator(regex=r"^[ER](\d+)$", message=_('Code does not comply'),)],)
    description = models.CharField(max_length=40)
    
    #0 Zone, 1 User
    type = models.IntegerField(default=0, choices=TYPES)

    # TYPE
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(9)])
    delay = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    
    def __str__(self):
            return self.name 


class Device(models.Model):

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
    
    name = models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=10, choices=TYPES)

    com = models.CharField(max_length=30, unique=True, choices=get_ports)
    baud_rate = models.IntegerField(default=9600, choices=BAUD_RATES)

    end_line = models.CharField(max_length=10, choices=END_LINES)

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