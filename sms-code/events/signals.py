
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .serializers import DecryptedEventSerializer

from .models import DecryptedEvent


@receiver(pre_save, sender=DecryptedEvent, dispatch_uid="update_event_status")
def update_event_status(sender, instance, **kwargs):
    old_instance = DecryptedEvent.objects.get(pk=instance.id)
    if instance.status != old_instance.status:
        # Old Value
        if old_instance.status == -1:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'events',
                {
                    'type':'remove_lock_event',
                    'message': instance.id
                }
            )

        # New Value
        if instance.status == -1: 
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'events',
                {
                    'type':'send_lock_event',
                    'message': DecryptedEventSerializer(instance).data
                }
            )
        elif instance.status == 0:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'events',
                {
                    'type':'send_uncommited_event',
                    'message': DecryptedEventSerializer(instance).data
                }
            )
       # elif old_instance.status == 
