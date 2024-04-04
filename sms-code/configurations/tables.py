import django_tables2 as tables

from .models import Device


class DeviceTable(tables.Table):
    class Meta:
        model = Device
        template_name = "django_tables2/bootstrap4-responsive.html"
        #fields = ("data", "device.name", "device.com", "created_at")
        
    view = tables.LinkColumn('configurations:device_detail',text="View", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('configurations:device_update',text="Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('configurations:device_delete',text="Delete", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })