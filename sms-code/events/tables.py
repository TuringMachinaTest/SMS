import django_tables2 as tables

from .models import DecryptedEvent, RawEvent


class RawEventTable(tables.Table):
    class Meta:
        model = RawEvent
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("id", "data", "device.name", "device.com", "created_at")
   
        
class DecryptedEventTable(tables.Table):
    class Meta:
        model = DecryptedEvent
        template_name = "django_tables2/bootstrap4-responsive.html"
        #fields = ("raw_event", "device.name", "device.com", "created_at")
        
    view = tables.LinkColumn('events:decryptedevent_detail',text="View", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
           
    edit = tables.LinkColumn('events:decryptedevent_update',text="Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })