from django.shortcuts import render
from rest_framework import viewsets, permissions

from events.filters import RawEventFilter
from events.models import RawEvent
from events.serializers import RawEventSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class EventViewSetV1(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RawEvent.objects.all().order_by('-created_at')
    serializer_class = RawEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RawEventFilter
