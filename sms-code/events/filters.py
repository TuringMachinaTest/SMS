import django_filters
from .models import DecryptedEvent, RawEvent
from django.db import models


class RawEventFilter(django_filters.FilterSet):
    class Meta:
        model = RawEvent
        fields = {'id': ["exact"], 'data':["contains",], 'device__name':["contains"], 'created_at':["range"], 'decrypted':["exact"], 'has_errors':["exact"]}
    
    @classmethod
    def filter_for_lookup(cls, f, lookup_type):
        # override date range lookups
        if isinstance(f, models.DateField) and lookup_type == 'range':
            return django_filters.DateTimeFromToRangeFilter, {}

        return super().filter_for_lookup(f, lookup_type)
        
        
class DecryptedEventFilter(django_filters.FilterSet):
    class Meta:
        model = DecryptedEvent
        fields = {'id': ["exact"], 'account' : ["exact"], 'status': ["exact"], 'created_at':["range"]}
        
    @classmethod
    def filter_for_lookup(cls, f, lookup_type):
        # override date range lookups
        if isinstance(f, models.DateField) and lookup_type == 'range':
            return django_filters.DateTimeFromToRangeFilter, {}

        return super().filter_for_lookup(f, lookup_type)