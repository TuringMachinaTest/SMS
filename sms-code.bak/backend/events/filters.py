import django_filters
from django.db import models

from django_filters import rest_framework as filters
from events.models import RawEvent


class RawEventFilter(filters.FilterSet):
    data = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = RawEvent
        fields = ['data']
