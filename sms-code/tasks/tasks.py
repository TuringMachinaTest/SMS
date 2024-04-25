from datetime import datetime, timedelta
import re
from serial import Serial
from django.core.cache import cache

from accounts.models import Account, AccountNote, AccountUser, Zone
from configurations.models import AlarmCode, Device
from events.models import DecryptedEvent, RawEvent
from events.serializers import DecryptedEventSerializer, RawEventSerializer
from events.utils import decrypt_event_mcdi, decrypt_event_surgard

from monitoring.utisl import send_message

def event_listener(device_no):
    
    devices = Device.objects.all()
    if devices.count() > device_no:
        device = devices[device_no]
    else:
        return
    
    end_line = device.end_line
    
    try:
        serial_port = Serial(device.com, device.baud_rate, timeout=10, exclusive=True)

        if not serial_port.is_open:
            serial_port.close()

            return
        # serial_port.open()
    except:
        return

    if end_line == "<DC1>":
        end_line = b'\x11'
    if end_line == "<DC2>":
        end_line = b'\x12'
    if end_line == "<DC3>":
        end_line = b'\x13'
    if end_line == "<DC4>":
        end_line = b'\x14'
    if end_line == "<CR>":
        end_line = b'\x0d'
            
    last_event = ""
    while True:  
        
        if cache.get("devices:kill-device:" + device.name) == "true":
            cache.delete("devices:kill-device:" + device.name)
            return
        
        if cache.get("devices:kill-device") == "all":
            return
        
        try:
            data = serial_port.read_until(end_line)
            #check event integrity
        except:
            break
        #    return
        
        # TODO: Check SUM
        if data:
            event = RawEvent()
            event.data = data.decode()
            event.device = device
            event.save()
            if event.pk:
                serial_port.write(b'\x06')

            #print(data.decode())
            send_message('events', 'send_raw_event', RawEventSerializer(event).data )


def dycrypt_events():
    
    for raw_event in RawEvent.objects.filter(decrypted=False).order_by('id')[:100]:
        
        if raw_event.device.type == "mcdi":
            (success, receiveer_no, line_no, account_no, alarm_code, partition, zone) = decrypt_event_mcdi(raw_event.data)
            protocole = -1
        elif raw_event.device.type == "surgard":
            (success, protocole, receiveer_no, line_no, account_no, alarm_code, partition, zone) = decrypt_event_surgard(raw_event.data)
            
        event = DecryptedEvent()
        event.raw_event = raw_event.id
        
        #success = success and receiveer_no is int and line_no is int and account_no is int and partition is int and zone is int
        
        try:
            receiveer_no = int(receiveer_no)
            line_no = int(line_no)
            account_no = int(account_no)
            if not re.search(r"^[ER](\d+)$", alarm_code):
                success = False
            #alarm_code = int(alarm_code)
            partition = int(partition)
            zone = int(zone)
            if protocole:
                protocole = int(protocole)
        except:
            success = False
            
        if success:
            event.custom = False
            event.protocole = protocole
            event.receiveer_no = receiveer_no
            event.line_no = line_no
            
            event.account = Account.objects.filter(pk=account_no).first()

            if partition >= 0 and partition <= 10:
                event.partition  = partition
            else:
                success = False
                
            if event.account:
                event.alarm_code = AlarmCode.objects.filter(code=alarm_code, partition=event.partition, account=event.account.id).first()
            else:
                success = False
                    
            if event.alarm_code and event.account:
                if  event.alarm_code.decryption_type == 0:
                    event.zone = Zone.objects.filter(code=zone, partition=event.partition, account=event.account.id).first()
                elif event.alarm_code.decryption_type == 1:
                    event.user = AccountUser.objects.filter(code=zone, partition=event.partition, account=event.account.id).first()
            else:
                success = False
                                
            event.success = success

            event.created_at = raw_event.created_at

            # If event.alarm_code.alarm_type is Auto Log
            if event.alarm_code and event.alarm_code.alarm_type == 1:
                # Change status to Saved
                event.status = 1
                event.save()
            else:
                # Else Save and Emmit unsaved event message
                event.save()
                send_message('events', 'send_uncommited_event', DecryptedEventSerializer(event).data )
            
        raw_event.decrypted = True
        raw_event.has_errors = not success
        raw_event.save()
        

def pending_events_timer():
    for event in DecryptedEvent.objects.filter(status=2, timer=True).order_by('id')[:100]:
        if event.updated_at + timedelta(minutes=event.timer_interval_minnutes, hours=event.timer_interval_hours) > datetime.now() :
            event.status = 0
            event.save()        
        
        
def follow_events_timer():
    for event in DecryptedEvent.objects.filter(status=3, timer=True).order_by('id')[:100]:
        if event.updated_at + timedelta(minutes=event.timer_interval_minnutes, hours=event.timer_interval_hours) > datetime.now() :
            event.status = 0
            event.save()
                    
        
def account_notes_timer():
    for note in AccountNote.objects.filter(timer=True).order_by('id')[:100]:
        if note.updated_at + timedelta(minutes=note.timer_interval_minutes, hours=note.timer_interval_hours) > datetime.now() :
            note.delete()
            
            
def check_delayed_events():
    for event in DecryptedEvent.objects.filter(has_return=False, delayed_return=False, handled_return_delay=False).order_by('id')[:100]:
        if event.created_at + timedelta(minutes=event.alarm_code.return_delay) > datetime.now():
            event.status = 4
            event.delayed_return = True
            event.save()
            
            
def check_periodic_events():
    for event in DecryptedEvent.objects.filter(is_last_periodic_event=True, delayed_periodic=False, handled_periodic_delay=False).order_by('id')[:100]:
        if event.created_at + timedelta(minutes=event.alarm_code.periodic_interval_minutes, hours=event.alarm_code.periodic_interval_hours) > datetime.now():
            event.status = 5
            event.delayed_periodic = True
            event.save()