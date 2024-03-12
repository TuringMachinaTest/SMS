import json

import serial.tools.list_ports
from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def get_ports():
    ports = serial.tools.list_ports.comports(include_links=False)
    result = {}
    result['/dev/pts/2'] = 'dev/pts/2'
    for port in ports:
        result[port.name] = port.device

    print(result)
    return result


class ContactIdCode(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30)


class DecryptionConfiguration(models.Model):
    name = models.CharField(max_length=30)
    decryption_mask = models.TextField()
    end_line = models.CharField(max_length=10, choices={"<CR>": "<CR>", "<DC4>": "<DC4>"})


# Create your models here.
class Device(models.Model):

    name = models.CharField(max_length=30, unique=True)
    ports_choices = get_ports()

    com = models.CharField(max_length=30, unique=True, blank=True, choices=get_ports)
    baud_rate = models.IntegerField()

    decryption_configuration = models.ForeignKey(DecryptionConfiguration, on_delete=models.SET_NULL, null=True)

    task = models.ForeignKey(PeriodicTask, null=True, on_delete=models.SET_NULL, blank=True)


@receiver(pre_delete, sender=Device)
def delete_task(sender, instance, using, **kwargs):
    instance.task.delete()


@receiver(pre_save, sender=Device)
def create_task(sender, instance, **kwargs):
    if not instance.id:

        schedule, created2 = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        instance.task = PeriodicTask.objects.create(
            interval=schedule,
            name=instance.name,
            task="events.tasks.message_listener",
            args=json.dumps([instance.name, instance.com, instance.baud_rate,
                             instance.decryption_configuration.end_line]),
            kwargs=json.dumps({
                })
        )


@receiver(post_save, sender=Device)
def update_task(sender, instance, created, **kwargs):
    if not created:
        schedule, created2 = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        instance.task.interval = schedule
        instance.task.name = instance.name
        instance.task.task = "events.tasks.message_listener"
        instance.task.args = json.dumps([instance.name, instance.com, instance.baud_rate,
                                         instance.decryption_configuration.end_line])
        instance.task.kwargs = json.dumps({
        })
        instance.task.save()




