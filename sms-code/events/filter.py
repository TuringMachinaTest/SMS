import django_filters
from .models import DecryptedEvent, RawEvent


class RawEventFilter(django_filters.FilterSet):
    class Meta:
        model = RawEvent
        fields = {'data':["contains",], 'device__name':["contains"], 'created_at':["range"]}

        
class DecryptedEventFilter(django_filters.FilterSet):
    class Meta:
        model = DecryptedEvent
        fields = {'status': ["exact"], 'created_at':["range"]}