import datetime

from celery import signals

from backend.celery import app

from serial import Serial
import redis
from contextlib import contextmanager

from configurations.models import Device
from events.models import RawEvent

redis_client = redis.Redis(host='localhost', port=6379)

@app.task(bind=True)
def message_listener(self, device_id, com, baud_rate, end_line):
    lock = redis_client.lock("device-lock:" + device_id)

    if lock.locked():
        print("Already Running")
        return

    if lock.acquire(blocking=True):
        try:
            serial_port = Serial(com, int(baud_rate), timeout=1)

            if not serial_port.is_open:
                serial_port.close()

                return
            # serial_port.open()
        except:
            lock.release()
            return

        print("Start Running")

        if end_line == "<CR>":
            end_line = b'\x13'

        message = ""
        while True:
            try:
                if not lock.locked():
                    return
                cc = serial_port.read()
                message += cc.decode()
                if cc == end_line:
                    raw_event = RawEvent()
                    raw_event.device = device_id
                    raw_event.data = message
                    raw_event.save()
                    if raw_event.pk is not None:
                        serial_port.write(b'\x06')
                    message = ""
                    # break
            except:
                break

        lock.release()

@signals.worker_shutdown.connect
@signals.worker_ready.connect
def remove_locks(**kwargs):
    devices = Device.objects.all()
    for device in devices:
        lock = redis_client.lock("device-lock:" + device.id)
        try:
            lock.release()
        except:
            pass
