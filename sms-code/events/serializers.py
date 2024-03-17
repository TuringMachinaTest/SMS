from configurations.serializers import DeviceSerializer
from .models import DecryptedEvent, RawEvent
from rest_framework import serializers


class RawEventSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    
    class Meta:
        model = RawEvent
        fields = '__all__'


class DecryptedEventSerializer(serializers.ModelSerializer):    
    class Meta:
        model = DecryptedEvent
        fields = '__all__'