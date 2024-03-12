from django.contrib import admin

from events.models import RawEvent


# Register your models here.
@admin.register(RawEvent)
class RawEventAdmin(admin.ModelAdmin):
    pass