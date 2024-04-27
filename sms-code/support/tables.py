import django_tables2 as tables

from support.models import ServiceOrder
from django.utils.translation import gettext as _


class ServiceOrderTable(tables.Table):
    class Meta:
        model = ServiceOrder
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("account", "summary", "status", "created_at", "closed_at")
        
    view = tables.LinkColumn('support:serviceorder_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('support:serviceorder_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('support:serviceorder_delete',text=_("Delete"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })