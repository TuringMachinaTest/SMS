import django_tables2 as tables

from .models import RawEvent


class RawEventTable(tables.Table):
    class Meta:
        model = RawEvent
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("data", "device.name", "device.com", "created_at")
        