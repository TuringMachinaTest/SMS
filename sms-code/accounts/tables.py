import django_tables2 as tables

from .models import Account


class AccountsTable(tables.Table):
    class Meta:
        model = Account
        template_name = "django_tables2/bootstrap4-responsive.html"
        fields = ("id", "name" )

    edit = tables.LinkColumn('account_update',text="View / Edit", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-warning'},
    })
    
    delete = tables.LinkColumn('account_delete',text="Delete", args=[tables.A('id')], attrs={
            'a': {'class': 'btn btn-danger'},
    })
