from serial import Serial
from django.core.cache import cache

from accounts.models import Account
from configurations.models import AlarmCode, Device
from events.models import DecryptedEvent, RawEvent
from events.utils import decrypt_event_mcdi, decrypt_event_surgard

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def event_listener(device_no):
    
    devices = Device.objects.all()
    if devices.count() > device_no:
        device = devices[device_no]
    else:
        return
    
    end_line = device.end_line
    
    try:
        serial_port = Serial(device.com, device.baud_rate, timeout=1)

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
            
    while True:  
        
        if cache.get("devices:kill-device:" + device.name) == "true":
            cache.delete("devices:kill-device:" + device.name)
            return
        
        if cache.get("devices:kill-device") == "all":
            return
        
        try:
            data = serial_port.read_until(end_line)
        except:
            return
        
        # TODO: Check SUM
        if data:
            event = RawEvent()
            event.data = data.decode()
            event.device = device
            event.save()
            if event.pk:
                serial_port.write(b'\x06')

            #print(data.decode())

def dycrypt_events():
    
    for raw_event in RawEvent.objects.filter(decrypted=False):
        
        if raw_event.device.type == "mcdi":
            (success, receiveer_no, line_no, account_no, alarm_code, partition, zone) = decrypt_event_mcdi(raw_event.data)
            protocole = None
        elif raw_event.device.type == "surgard":
            (success, protocole, receiveer_no, line_no, account_no, alarm_code, partition, zone) = decrypt_event_surgard(raw_event.data)
            
        event = DecryptedEvent()
        event.raw_event = raw_event

        if success:
            event.receiveer_no = receiveer_no
            event.line_no = line_no
            
            event.alarm_code = AlarmCode.objects.filter(code=alarm_code).first()
            event.account = Account.objects.filter(pk=account_no).first()
            
            event.partition  = partition
            
            event.success = True
            #event.user = AlarmCode.objects.get(keypad_code=zone)

            event.save()
        
        raw_event.decrypted = True
        raw_event.save()
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'test',
            {
                'type':'chat_message',
                'message':raw_event.data
            }
        )