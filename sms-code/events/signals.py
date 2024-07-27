from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from accounts.models import AccountNote

from .serializers import DecryptedEventSerializer

from .models import DecryptedEvent
from monitoring.utisl import send_message

@receiver(pre_save, sender=DecryptedEvent, dispatch_uid="update_event_status")
def update_event_status(sender, instance, **kwargs):
    
    old_instance = DecryptedEvent.objects.filter(pk=instance.id).first()
    
    if old_instance == None:
        send_message('alerts', 'send_event_alert', DecryptedEventSerializer(instance).data )
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
        elif old_instance.status == 4:
            send_message('events', 'remove_delayed_event', instance.id ) 
        elif old_instance.status == 5:
            send_message('events', 'remove_delayed_periodic_event', instance.id ) 
               
        # New Value
        if instance.status == -1: 
            send_message('events', 'send_lock_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 0:
            send_message('events', 'send_uncommited_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 2:
            send_message('events', 'send_pending_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 3:
            send_message('events', 'send_follow_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 4:
            send_message('events', 'send_delayed_event', DecryptedEventSerializer(instance).data )
        elif instance.status == 5:
            send_message('events', 'send_delayed_periodic_event', DecryptedEventSerializer(instance).data )            
       # elif old_instance.status == 


@receiver(post_save, sender=DecryptedEvent, dispatch_uid="save_account_note")
def save_account_note(sender, instance, **kwargs):
    
    account_note = AccountNote.objects.filter(account=instance.account, decrypted_event=instance.id).first()
    
    if account_note and instance.account_note and instance.account_note.strip() != "":
      account_note.note = instance.account_note
      account_note.timer=instance.account_note_timer, 
      account_note.timer_interval_minutes=instance.note_timer_interval_minnutes, 
      account_note.timer_interval_hours=instance.note_timer_interval_hours
      account_note.save()  
    
    elif instance.account_note and instance.account_note.strip() != "":
        account_note = AccountNote(
            account=instance.account,
            decrypted_event=instance.id, 
            note=instance.account_note, 
            timer=instance.account_note_timer, 
            timer_interval_minutes=instance.note_timer_interval_minnutes, 
            timer_interval_hours=instance.note_timer_interval_hours
        )
        account_note.save()