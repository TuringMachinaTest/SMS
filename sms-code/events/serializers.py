from accounts.serializers import AccountSerializer
from configurations.serializers import AlarmCodeSerializer, DeviceSerializer
from .models import DecryptedEvent, RawEvent
from rest_framework import serializers


class RawEventSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    
    class Meta:
        model = RawEvent
        fields = '__all__'


class DecryptedEventSerializer(serializers.ModelSerializer): 
       
    account = AccountSerializer()
    alarm_code = AlarmCodeSerializer()
    
    class Meta:
        model = DecryptedEvent
        fields = '__all__'