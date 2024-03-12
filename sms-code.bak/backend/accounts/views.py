import threading

from django.http import JsonResponse
from django.shortcuts import render

from . import tasks
from .models import City, Account, AccountUser
from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from logging import getLogger

logger = getLogger(__name__)

from .serializers import CitySerializer, AccountSerializer, AccountUserSerializer


# Create your views here.


class CityViewSetV1(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class AccountViewSetV1(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['name']


class AccountUserViewSetV1(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all().order_by('name')
    serializer_class = AccountUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['account', 'partition']
    search_fields = []
