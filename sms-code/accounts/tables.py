import django_tables2 as tables

from .models import Account, City, Group, InstallationCompany
from django.utils.translation import gettext as _


class AccountsTable(tables.Table):
    class Meta:
        model = Account
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("id", "name" )

    view = tables.LinkColumn('accounts:account_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('accounts:account_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('accounts:account_delete',text=_("Delete"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })


class InstallationCompanyTable(tables.Table):
    class Meta:
        model = InstallationCompany
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("name", "phone_number1", "phone_number2")
        
    view = tables.LinkColumn('accounts:installationcompany_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('accounts:installationcompany_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('accounts:installationcompany_delete',text=_("Delete"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })


class CityTable(tables.Table):
    class Meta:
        model = City
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("name",)
        
    view = tables.LinkColumn('accounts:city_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('accounts:city_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('accounts:city_delete',text=_("Delete"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })
    
    
class GroupTable(tables.Table):
    class Meta:
        model = Group
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("name",)
        
    view = tables.LinkColumn('accounts:group_detail',text=_("View"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('accounts:group_update',text=_("Edit"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('accounts:group_delete',text=_("Delete"), args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })