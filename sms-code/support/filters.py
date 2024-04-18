import django_filters

from support.models import ServiceOrder



class ServiceOrderFilter(django_filters.FilterSet):
    class Meta:
        model = ServiceOrder
        fields = {'account':["exact"]}