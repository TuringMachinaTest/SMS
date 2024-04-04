from .models import AlarmCode, Device
from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class AlarmCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmCode
        fields = '__all__'