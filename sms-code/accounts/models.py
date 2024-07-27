from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

from phonenumber_field import modelfields

from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords

import configurations


class City(models.Model):
    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name 
    
    
class Group(models.Model):
    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name 
    
     
class InstallationCompany(models.Model):
    
    class Meta:
        verbose_name = _("Installation Company")
        verbose_name_plural = _("Installation Companies")
            
    name = models.CharField(max_length=30, blank=True, verbose_name = _("Company Name"))
    phone_number1 = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True, verbose_name=_("Phone Number 1"))
    phone_number2 = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True, verbose_name=_("Phone Number 2"))
    def __str__(self):
        return self.name 
    
    
class Account(models.Model):
    
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
    
    id = models.PositiveIntegerField(primary_key=True, verbose_name=_("Account ID"))
    name = models.CharField(max_length=40, verbose_name=_("Account Name"))
    
    active = models.BooleanField(default=True, verbose_name=_("Active"))

    address_line1 = models.CharField(max_length=30, blank=True, verbose_name=_("Address Line 1"))
    address_line2 = models.CharField(max_length=30, blank=True ,verbose_name=_("Address Line 2"))
    address_line3 = models.CharField(max_length=30, blank=True, verbose_name=_("Address Line 3"))

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("City"))

    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("Zip Code"))

    email = models.EmailField(max_length=30, blank=True, verbose_name=_("Email"))

    phone_number1 = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True, verbose_name=_("Phone Number 1"))
    phone_number2 = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True, verbose_name=_("Phone Number 2"))
    whatsapp_number = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True, verbose_name=_("Whatsapp Number"))

    # Accounts MISC
    security_number = models.CharField(max_length=20, blank=True, verbose_name=_("Security Number"))

    memo = models.TextField(max_length=120, blank=True, verbose_name=_("Memo"))

    police_number1 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Police Number 1"))
    police_number2 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Police Number 2"))
    police_number3 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Police Number 3"))

    fire_dept_number1 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Fire Dept Number 1"))
    fire_dept_number2 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Fire Dept Number 2"))
    fire_dept_number3 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Fire Dept Number 3"))

    emergency_number1 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Emergency Number 1"))
    emergency_number2 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Emergency Number 2"))
    emergency_number3 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True, verbose_name=_("Emergency Number 3"))

    # Partitions
    partition_name0 = models.CharField(max_length=30, default="Default", verbose_name=_("Partition Name 0"))
    partition_name1 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 1"))
    partition_name2 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 2"))
    partition_name3 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 3"))
    partition_name4 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 4"))
    partition_name5 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 5"))
    partition_name6 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 6"))
    partition_name7 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 7"))
    partition_name8 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 8"))
    partition_name9 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 9"))
    partition_name10 = models.CharField(max_length=30, blank=True, verbose_name=_("Partition Name 10"))
    
    # Alarm Codes
    copy_alarm_codes = models.BooleanField(default=False, verbose_name=_("Copy Alarm Codes"))
    copy_alarm_codes_from = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Copy Alarm Codes From"))
    
    # Installation
    installation_company = models.ForeignKey(InstallationCompany, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Installation Company"))

    installation_date = models.DateField(null=True, blank=True, verbose_name=_("Installation Date"))
    installation_note = models.TextField(max_length=120, blank=True, verbose_name=_("Installation Note"))
    receiver_phone_number = models.CharField(max_length=20, blank=True, verbose_name=_("Receiver Phone Number"))
    transmitter_phone_number = models.CharField(max_length=20, blank=True, verbose_name=_("Transmitter Phone Number"))

    # Groups
    groups = models.ManyToManyField(Group, blank=True, related_name="accounts", verbose_name=_("Groups"))

    # Accounts Control
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Created By"))
    
    history = HistoricalRecords(verbose_name=_("History"))
    
    def save(self, *args, **kwargs):
        
        if not self._state.adding and self.copy_alarm_codes and self.copy_alarm_codes_from:
            alarm_codes = configurations.models.AlarmCode.objects.filter(account=self.copy_alarm_codes_from)
            for alarm_code in alarm_codes:
                new_alarm_code = configurations.models.AlarmCode(
                    account=self,  #Account(id=self.id), 
                    code=alarm_code.code,
                    description=alarm_code.description,
                    partition=alarm_code.partition,
                    alarm_type=alarm_code.alarm_type,
                    decryption_type=alarm_code.decryption_type,
                    has_return=alarm_code.has_return,
                    return_delay_minutes=alarm_code.return_delay_minutes,
                    return_delay_hours=alarm_code.return_delay_hours,
                    is_periodic=alarm_code.is_periodic,
                    periodic_interval_minutes=alarm_code.periodic_interval_minutes,
                    periodic_interval_hours=alarm_code.periodic_interval_hours,
                )
                new_alarm_code.save()
                
        self.copy_alarm_codes = False
        self.copy_alarm_codes_from = None
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id) + " : " + self.name 
 
 
class AccountNote(models.Model):
    
    class Meta:
        verbose_name = _("Account Note")
        verbose_name_plural = _("Account Notes")
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_("Account"))
    decrypted_event = models.PositiveBigIntegerField(default=0, verbose_name=_("Decrypted Event"))
    
    note = models.TextField(max_length=120, null=True, blank=True, verbose_name=_("Note"))
    
    timer = models.BooleanField(default=False, db_index=True, verbose_name=_("Timer"))
    timer_interval_minutes = models.PositiveIntegerField(default=0, verbose_name=_("Minutes"))
    timer_interval_hours = models.PositiveIntegerField(default=0, verbose_name=_("Hours"))

    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Created By"))

    def __str__(self):
        return self.note    


class AccountUser(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'partition', 'code'], name='accounts.accountuser.unique_id')
        ]
        verbose_name = _("Account User")
        verbose_name_plural = _("Account Users")
        
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_("Account"))
    partition = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name=_("Partition"))

    # Information
    name = models.CharField(max_length=40, verbose_name=_("Name"))
    code = models.PositiveIntegerField(verbose_name=_("Code"))

    in_out_codes = models.CharField(max_length=20, blank=True, verbose_name=_("In-Out Codes"))
    password = models.CharField(max_length=15, blank=True, verbose_name=_("Password"))

    phone_number1 = models.CharField(max_length=20, blank=True, verbose_name=_("Phone Number 1"))
    phone_number2 = models.CharField(max_length=20, blank=True, verbose_name=_("Phone Number 2"))
    phone_number3 = models.CharField(max_length=20, blank=True, verbose_name=_("Phone Number 3"))
    
    title1 = models.CharField(max_length=150, blank=True, verbose_name=_("Title"))
    title2 = models.CharField(max_length=150, blank=True, verbose_name=_("Title"))
    title3 = models.CharField(max_length=150, blank=True, verbose_name=_("Title"))

    # Control

    holiday_begins = models.DateField(null=True, blank=True, verbose_name=_("Holiday Begins"))
    holiday_ends = models.DateField(null=True, blank=True, verbose_name=_("Holiday Ends"))
    
    keypad_code = models.CharField(max_length=6, blank=True, verbose_name=_("Keypad Code"))

    hot_user = models.BooleanField(default=False, verbose_name=_("Hot User"))

    authorized_days_sat = models.BooleanField(default=False, verbose_name=_("Saturday"))
    authorized_days_sun = models.BooleanField(default=False, verbose_name=_("Sunday"))
    authorized_days_mon = models.BooleanField(default=False, verbose_name=_("Monday"))
    authorized_days_tue = models.BooleanField(default=False, verbose_name=_("Tuesday"))
    authorized_days_wed = models.BooleanField(default=False, verbose_name=_("Wednesday"))
    authorized_days_thu = models.BooleanField(default=False, verbose_name=_("Thursday"))
    authorized_days_fri = models.BooleanField(default=False, verbose_name=_("Friday"))

    # Users Control
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Created By"))
    
    
    def get_autherized_day(self, day_of_the_week):
        if day_of_the_week == 0:
            return self.authorized_days_mon
        elif day_of_the_week == 1:
            return self.authorized_days_tue
        elif day_of_the_week == 2:
            return self.authorized_days_wed
        elif day_of_the_week == 3:
            return self.authorized_days_thu
        elif day_of_the_week == 4:
            return self.authorized_days_fri
        elif day_of_the_week == 5:
            return self.authorized_days_sat
        elif day_of_the_week == 6:
            return self.authorized_days_sun 
    
    def __str__(self):
        return self.name 
    
    
class Zone(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'partition', 'code'], name='accounts.zone.unique_id')
        ]

        verbose_name = _("Zone")
        verbose_name_plural = _("Zones")
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_("Account"))
    partition = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name=_("Partition"))

    name = models.CharField(max_length=30, verbose_name=_("Name"))
    code = models.PositiveIntegerField(verbose_name=_("Code"))
        
    def __str__(self):
        return self.name 