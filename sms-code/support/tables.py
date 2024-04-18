import django_tables2 as tables

from support.models import ServiceOrder


class ServiceOrderTable(tables.Table):
    class Meta:
        model = ServiceOrder
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("account", "summary", "status", "created_at")
        
    view = tables.LinkColumn('support:serviceorder_detail',text="View", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('support:serviceorder_update',text="Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('support:serviceorder_delete',text="Delete", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })