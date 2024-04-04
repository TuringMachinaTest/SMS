from django.db.models.signals import pre_save
from django.dispatch import receiver

from .serializers import DecryptedEventSerializer

from .models import DecryptedEvent
from monitoring.utisl import send_message

@receiver(pre_save, sender=DecryptedEvent, dispatch_uid="update_event_status")
def update_event_status(sender, instance, **kwargs):
    
    old_instance = DecryptedEvent.objects.filter(pk=instance.id).first()
    
    if old_instance == None:
        return
    
    if instance.status != old_instance.status:
        # Old Value
        if old_instance.status == -1:
            send_message('events', 'remove_lock_event', instance.id )
        elif old_instance.status == 0:
            send_message('events', 'remove_uncommited_event', instance.id )
        elif old_instance.status == 2:
            send_message('events', 'remove_pending_event', instance.id )
        elif old_instance.status == 3:
            send_message('events', 'remove_follow_event', instance.id )       
        
        # New Value
        if instance.status == -1: 
            send_message('events', 'send_lock_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 0:
            send_message('events', 'send_uncommited_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 2:
            send_message('events', 'send_pending_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 3:
            send_message('events', 'send_follow_event', DecryptedEventSerializer(instance).data )
            
       # elif old_instance.status == 
