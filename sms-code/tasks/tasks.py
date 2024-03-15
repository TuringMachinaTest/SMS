from base64 import encode
from serial import Serial

from configurations.models import Device
from events.models import RawEvent


def event_listener(device_no):
    
    device = Device.objects.all()[device_no]
    
    end_line = "<CR>"
    
    try:
        serial_port = Serial("COM2", int(115200), timeout=1)

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
            
    try:    
        while True:       
            data = serial_port.read_until(end_line)
            # TODO: Check SUM
            if data:
                event = RawEvent()
                event.data = data.decode()
                event.device = device
                event.save()
                if event.pk:
                    serial_port.write(b'\x06')

                print(data.decode())
    except:
        pass