import json
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .utils import get_ports


class AlarmCode(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
            return self.name 


class DecryptionConfiguration(models.Model):
    name = models.CharField(max_length=30)
    decryption_mask = models.TextField()
    end_line = models.CharField(max_length=10, choices={"<CR>": "<CR>", "<DC4>": "<DC4>"})
    
    def __str__(self):
            return self.name


class Device(models.Model):

    name = models.CharField(max_length=30, unique=True)

    com = models.CharField(max_length=30, unique=True, blank=True, choices=get_ports)
    baud_rate = models.IntegerField(default=9600)

    decryption_configurations = models.ManyToManyField(DecryptionConfiguration, null=True)

    task = models.ForeignKey(PeriodicTask, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
            return self.name
        

@receiver(pre_delete, sender=Device)
def delete_device_task(sender, instance, using, **kwargs):
    instance.task.delete()

@receiver(pre_save, sender=Device)
def create_device_task(sender, instance, **kwargs):
    if not instance.id:

        schedule, created2 = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        instance.task = PeriodicTask.objects.create(
            interval=schedule,
            name=instance.name,
            task="events.tasks.message_listener",
            args=json.dumps([
                instance.name, instance.com, instance.baud_rate,
                instance.decryption_configurations
            ]),
            kwargs=json.dumps({
                
            })
        )
        
@receiver(post_save, sender=Device)
def update_device_task(sender, instance, created, **kwargs):
    if not created:
        schedule, created2 = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        instance.task.interval = schedule
        instance.task.name = instance.name
        instance.task.task = "events.tasks.message_listener"
        args=json.dumps([
            instance.name, instance.com, instance.baud_rate,
            instance.decryption_configurations
        ]),
        kwargs=json.dumps({
            
        })
        instance.task.save()