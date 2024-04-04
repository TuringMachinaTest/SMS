import signal
import sys
from django.core.cache import cache

from django.dispatch import receiver
from django.utils.autoreload import file_changed

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from .tasks import dycrypt_events, event_listener


scheduler = BackgroundScheduler()

def add_jobs():
    for device_no in range(5):
        scheduler.add_job(event_listener, 'interval', seconds=10, args=[device_no], max_instances=1)
    
    scheduler.add_job(dycrypt_events, 'interval', seconds=5, args=[], max_instances=1)


def kill(signal, frame):
    scheduler.shutdown(wait=False)
    cache.set("devices:kill-device", "all")
    sys.exit(0) 

def start():
    add_jobs()
    # scheduler = BackgroundScheduler()    
    scheduler.start()
    cache.delete("devices:kill-device")

    
signal.signal(signal.SIGINT, kill)
signal.signal(signal.SIGTERM, kill)
