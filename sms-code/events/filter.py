import django_filters
from .models import RawEvent


class RawEventFilter(django_filters.FilterSet):
    class Meta:
        model = RawEvent
        fields = {'data':["contains",], 'device__name':["contains"], 'created_at':["range"]}