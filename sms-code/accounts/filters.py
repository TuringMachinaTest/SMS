import django_filters

from .models import Account


class AccountFilter(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = {'id':["contains"] ,'name':["contains"], 'city': ["exact"]}
