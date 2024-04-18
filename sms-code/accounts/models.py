from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

from phonenumber_field import modelfields

from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords


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
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    address_line1 = models.CharField(max_length=30, blank=True)
    address_line2 = models.CharField(max_length=30, blank=True)
    address_line3 = models.CharField(max_length=30, blank=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    zip_code = models.CharField(max_length=10, blank=True)

    email = models.EmailField(max_length=30, blank=True)

    phone_number1 = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True)
    phone_number2 = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True)
    whatsapp_number = modelfields.PhoneNumberField(region="SY", max_length=20, blank=True)

    # Accounts MISC
    security_number = models.CharField(max_length=20, blank=True)

    memo = models.TextField(max_length=120, blank=True)

    police_number1 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)
    police_number2 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)
    police_number3 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)

    fire_dept_number1 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)
    fire_dept_number2 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)
    fire_dept_number3 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)

    emergency_number1 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)
    emergency_number2 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)
    emergency_number3 = modelfields.PhoneNumberField(region="SY",max_length=20, blank=True)

    # Partitions
    partition_name0 = models.CharField(max_length=30, default="Default")
    partition_name1 = models.CharField(max_length=30, blank=True)
    partition_name2 = models.CharField(max_length=30, blank=True)
    partition_name3 = models.CharField(max_length=30, blank=True)
    partition_name4 = models.CharField(max_length=30, blank=True)
    partition_name5 = models.CharField(max_length=30, blank=True)
    partition_name6 = models.CharField(max_length=30, blank=True)
    partition_name7 = models.CharField(max_length=30, blank=True)
    partition_name8 = models.CharField(max_length=30, blank=True)
    partition_name9 = models.CharField(max_length=30, blank=True)
    partition_name10 = models.CharField(max_length=30, blank=True)
    
    # Installation
    installation_company = models.ForeignKey(InstallationCompany, on_delete=models.SET_NULL, null=True, blank=True)

    installation_date = models.DateField(null=True, blank=True)
    installation_note = models.TextField(max_length=120, blank=True)
    receiver_phone_number = models.CharField(max_length=20, blank=True)
    transmitter_phone_number = models.CharField(max_length=20, blank=True)

    # Groups
    groups = models.ManyToManyField(Group, blank=True, related_name="accounts")

    # Accounts Control
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    
    history = HistoricalRecords()
    
    def __str__(self):
        return str(self.id) + " : " + self.name 
    

class AccountUser(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'partition', 'code'], name='accounts.accountuser.unique_id')
        ]
        verbose_name = _("Account User")
        verbose_name_plural = _("Account Users")
        
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    partition = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    # Information
    name = models.CharField(max_length=40)
    code = models.IntegerField()

    in_out_codes = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=15, blank=True)

    phone_number1 = models.CharField(max_length=20, blank=True)
    phone_number2 = models.CharField(max_length=20, blank=True)
    phone_number3 = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=150, blank=True)

    # Control

    holiday_begins = models.DateField(null=True, blank=True)
    holiday_ends = models.DateField(null=True, blank=True)
    
    keypad_code = models.CharField(max_length=6, blank=True)

    hot_user = models.BooleanField(default=False)

    authorized_days_sat = models.BooleanField(default=False, verbose_name="Saturday")
    authorized_days_sun = models.BooleanField(default=False)
    authorized_days_mon = models.BooleanField(default=False)
    authorized_days_tue = models.BooleanField(default=False)
    authorized_days_wed = models.BooleanField(default=False)
    authorized_days_thu = models.BooleanField(default=False)
    authorized_days_fri = models.BooleanField(default=False)

    # Users Control
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
        
    def __str__(self):
        return self.name 
    
    
class Zone(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'partition', 'code'], name='accounts.zone.unique_id')
        ]

        verbose_name = _("Zone")
        verbose_name_plural = _("Zones")
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    partition = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    name = models.CharField(max_length=30)
    code = models.IntegerField()
        
    def __str__(self):
        return self.name 