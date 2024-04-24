from datetime import timedelta
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


class Schedule(models.Model):
    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedules")
        
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True, verbose_name=_("Account"))
    partition = models.IntegerField(default=0, db_index=True, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name=_("Partition"))
    
    is_open_saturday = models.BooleanField(default=False, verbose_name=_("Open Saturday"))
    opening_saturday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Saturday"))
    delay_opning_saturday = models.IntegerField(default=0, verbose_name=_("Delay Open Saturday"))
    closing_saturday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Saturday"))
    delay_closing_saturday = models.IntegerField(default=0, verbose_name=_("Delay Open Saturday"))

    is_open_sunday = models.BooleanField(default=False, verbose_name=_("Open Sunday"))
    opening_sunday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Sunday"))
    delay_opning_sunday = models.IntegerField(default=0, verbose_name=_("Delay Open Sunday"))
    closing_sunday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Sunday"))
    delay_closing_sunday = models.IntegerField(default=0, verbose_name=_("Delay Open Sunday"))
    
    is_open_monday = models.BooleanField(default=False, verbose_name=_("Open Monday"))
    opening_monday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Monday"))
    delay_opning_monday = models.IntegerField(default=0, verbose_name=_("Delay Open Monday"))
    closing_monday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Monday"))
    delay_closing_monday = models.IntegerField(default=0, verbose_name=_("Delay Open Monday"))

    is_open_tuesday = models.BooleanField(default=False, verbose_name=_("Open Tuesday"))
    opening_tuesday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Tuesday"))
    delay_opning_tuesday = models.IntegerField(default=0, verbose_name=_("Delay Open Tuesday"))
    closing_tuesday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Tuesday"))
    delay_closing_tuesday = models.IntegerField(default=0, verbose_name=_("Delay Open Tuesday"))

    is_open_wednesday = models.BooleanField(default=False, verbose_name=_("Open Wednesday"))
    opening_wednesday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Wednesday"))
    delay_opning_wednesday = models.IntegerField(default=0, verbose_name=_("Delay Open Wednesday"))
    closing_wednesday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Wednesday"))
    delay_closing_wednesday = models.IntegerField(default=0, verbose_name=_("Delay Open Wednesday"))

    is_open_thursday = models.BooleanField(default=False, verbose_name=_("Open Thursday"))
    opening_thursday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Thursday"))
    delay_opning_thursday = models.IntegerField(default=0, verbose_name=_("Delay Open Thursday"))
    closing_thursday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Thursday"))
    delay_closing_thursday = models.IntegerField(default=0, verbose_name=_("Delay Open Thursday"))

    is_open_friday = models.BooleanField(default=False, verbose_name=_("Open Friday"))
    opening_friday = models.TimeField(null=True, blank=True, verbose_name=_("Opening Friday"))
    delay_opning_friday = models.IntegerField(default=0, verbose_name=_("Delay Open Friday"))
    closing_friday = models.TimeField(null=True, blank=True, verbose_name=_("Closing Friday"))
    delay_closing_friday = models.IntegerField(default=0, verbose_name=_("Delay Open Friday"))

    def get_opening_time(self, day_of_week):
        if day_of_week == 0:
            return self.opening_monday - timedelta(minutes=self.delay_opning_monday), self.opening_monday + timedelta(minutes=self.delay_opning_monday)
        elif day_of_week == 1:
            return self.opening_tuesday - timedelta(minutes=self.delay_opning_tuesday), self.opening_tuesday + timedelta(minutes=self.delay_opning_tuesday)
        elif day_of_week == 2:
            return self.opening_wednesday - timedelta(minutes=self.delay_opning_wednesday), self.opening_wednesday + timedelta(minutes=self.delay_opning_wednesday)
        elif day_of_week == 3:
            return self.opening_thursday - timedelta(minutes=self.delay_opning_thursday), self.opening_thursday + timedelta(minutes=self.delay_opning_thursday)
        elif day_of_week == 4:
            return self.opening_friday - timedelta(minutes=self.delay_opning_friday), self.opening_friday + timedelta(minutes=self.delay_opning_friday)
        elif day_of_week == 5:
            return self.opening_saturday - timedelta(minutes=self.delay_opning_saturday), self.opening_saturday + timedelta(minutes=self.delay_opning_saturday)
        elif day_of_week == 6:
            return self.opening_sunday - timedelta(minutes=self.delay_opning_sunday), self.opening_sunday + timedelta(minutes=self.delay_opning_sunday)
    
    def get_closing_time(self, day_of_week):
        if day_of_week == 0:
            return self.closing_monday - timedelta(minutes=self.delay_closing_monday), self.closing_monday + timedelta(minutes=self.delay_closing_monday)
        elif day_of_week == 1:
            return self.closing_tuesday - timedelta(minutes=self.delay_closing_tuesday), self.closing_tuesday + timedelta(minutes=self.delay_closing_tuesday)
        elif day_of_week == 2:
            return self.closing_wednesday - timedelta(minutes=self.delay_closing_wednesday), self.closing_wednesday + timedelta(minutes=self.delay_closing_wednesday)
        elif day_of_week == 3:
            return self.closing_thursday - timedelta(minutes=self.delay_closing_thursday), self.closing_thursday + timedelta(minutes=self.delay_closing_thursday)
        elif day_of_week == 4:
            return self.closing_friday - timedelta(minutes=self.delay_closing_friday), self.closing_friday + timedelta(minutes=self.delay_closing_friday)
        elif day_of_week == 5:
            return self.closing_saturday - timedelta(minutes=self.delay_closing_saturday), self.closing_saturday + timedelta(minutes=self.delay_closing_saturday)
        elif day_of_week == 6:
            return self.closing_sunday - timedelta(minutes=self.delay_closing_sunday), self.closing_sunday + timedelta(minutes=self.delay_closing_sunday)
        
    def get_is_open(self, day_of_week):
        if day_of_week == 0:
            return self.is_open_monday
        elif day_of_week == 1:
            return self.is_open_tuesday
        elif day_of_week == 2:
            return self.is_open_wednesday
        elif day_of_week == 3:
            return self.is_open_thursday
        elif day_of_week == 4:
            return self.is_open_friday
        elif day_of_week == 5:
            return self.is_open_saturday
        elif day_of_week == 6:
            return self.is_open_sunday
    
    def __str__(self):
        return self.name


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