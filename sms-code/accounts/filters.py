import django_filters

from .models import Account, City, InstallationCompany


class AccountFilter(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = {'id':["contains"] ,'name':["contains"], 'city': ["exact"]}


class InstallationCompanyFilter(django_filters.FilterSet):
    class Meta:
        model = InstallationCompany
        fields = {'name':["contains"], 'phone_number1': ["contains"], 'phone_number2': ["contains"]}
        

class CityFilter(django_filters.FilterSet):
    class Meta:
        model = City
        fields = {'name':["contains"]}