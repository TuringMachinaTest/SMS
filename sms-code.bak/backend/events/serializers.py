from rest_framework import serializers

from events.models import RawEvent


class RawEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RawEvent
        fields = ['id', 'data', 'device_name', 'created_at']
