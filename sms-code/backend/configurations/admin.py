from django.contrib import admin

from configurations.models import Device, DecryptionConfiguration


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass


@admin.register(DecryptionConfiguration)
class DecryptionConfigurationAdmin(admin.ModelAdmin):
    pass
