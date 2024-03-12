from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class City(models.Model):
    class Meta:
        verbose_name_plural = "Cities"

    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name 


class InstallationCompany(models.Model):
    
    name = models.CharField(max_length=30)
    
    phone_number1 = models.CharField(max_length=20, blank=True)
    phone_number2 = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
    
    


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    address_line1 = models.CharField(max_length=30, blank=True)
    address_line2 = models.CharField(max_length=30, blank=True)
    address_line3 = models.CharField(max_length=30, blank=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    zip_code = models.CharField(max_length=10, blank=True)

    email = models.EmailField(max_length=30, blank=True)

    phone_number1 = models.CharField(max_length=20, blank=True)
    phone_number2 = models.CharField(max_length=20, blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)

    # Accounts MISC
    security_number = models.CharField(max_length=20, blank=True)

    memo = models.CharField(max_length=120, blank=True)

    police_number1 = models.CharField(max_length=20, blank=True)
    police_number2 = models.CharField(max_length=20, blank=True)
    police_number3 = models.CharField(max_length=20, blank=True)

    fire_dept_number1 = models.CharField(max_length=20, blank=True)
    fire_dept_number2 = models.CharField(max_length=20, blank=True)
    fire_dept_number3 = models.CharField(max_length=20, blank=True)

    emergency_number1 = models.CharField(max_length=20, blank=True)
    emergency_number2 = models.CharField(max_length=20, blank=True)
    emergency_number3 = models.CharField(max_length=20, blank=True)

    # Partitions
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
    installation_note = models.CharField(max_length=120, blank=True)
    receiver_phone_number = models.CharField(max_length=20, blank=True)
    transmitter_phone_number = models.CharField(max_length=20, blank=True)

    # Accounts Control
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name 
    

class AccountUser(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'partition', 'name'], name='unique_id')
        ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    partition = models.IntegerField(default=0)

    # Information
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=15, blank=True)

    in_out_codes = models.CharField(max_length=20, blank=True)

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