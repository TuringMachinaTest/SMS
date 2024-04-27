import django_tables2 as tables

from .models import DecryptedEvent, RawEvent
from django.utils.translation import gettext as _


class RawEventTable(tables.Table):
    class Meta:
        model = RawEvent
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("id", "data", "device.name", "device.com", "created_at")
        
    view = tables.LinkColumn('events:rawevent_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
        
        
class DecryptedEventTable(tables.Table):
    class Meta:
        model = DecryptedEvent
        template_name = "django_tables2/bootstrap4-responsive.html"
        #fields = ("raw_event", "device.name", "device.com", "created_at")
        
    view = tables.LinkColumn('events:decryptedevent_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
           
    edit = tables.LinkColumn('events:decryptedevent_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })