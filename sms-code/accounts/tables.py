import django_tables2 as tables

from .models import Account, City, InstallationCompany


class AccountsTable(tables.Table):
    class Meta:
        model = Account
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("id", "name" )

    view = tables.LinkColumn('account_details',text="View", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('account_update',text="Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('account_delete',text="Delete", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })


class InstallationCompanyTable(tables.Table):
    class Meta:
        model = InstallationCompany
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("name", "phone_number1", "phone_number2")
        
    view = tables.LinkColumn('installation_company_details',text="View", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('installation_company_update',text="Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('installation_company_delete',text="Delete", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })


class CityTable(tables.Table):
    class Meta:
        model = City
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("name",)
        
    view = tables.LinkColumn('city_details',text="View", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-info'},
    })
    
    edit = tables.LinkColumn('city_update',text="Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('city_delete',text="Delete", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })