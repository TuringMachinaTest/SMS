import django_tables2 as tables

from .models import Device
from django.utils.translation import gettext as _


class DeviceTable(tables.Table):
    class Meta:
        model = Device
        template_name = "django_tables2/bootstrap4-responsive.html"
        #fields = ("data", "device.name", "device.com", "created_at")
        
    view = tables.LinkColumn('configurations:device_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('configurations:device_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('configurations:device_delete',text=_("Delete"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })