import signal
import sys
from django.core.cache import cache

from django.dispatch import receiver
from django.utils.autoreload import file_changed

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from .tasks import check_delayed_periodic_events, check_delayed_return_events, dycrypt_events, event_listener, pending_events_timer, follow_events_timer, account_notes_timer


scheduler = BackgroundScheduler()

def add_jobs():
    for device_no in range(5):
        scheduler.add_job(event_listener, 'interval', seconds=10, args=[device_no], max_instances=1)
    
    scheduler.add_job(dycrypt_events, 'interval', seconds=5, args=[], max_instances=1)
    
    scheduler.add_job(pending_events_timer, 'interval', seconds=60, args=[], max_instances=1)
    scheduler.add_job(follow_events_timer, 'interval', seconds=60, args=[], max_instances=1)
    scheduler.add_job(account_notes_timer, 'interval', seconds=60, args=[], max_instances=1)
    
    scheduler.add_job(check_delayed_return_events, 'interval', seconds=60, args=[], max_instances=1)
    scheduler.add_job(check_delayed_periodic_events, 'interval', seconds=60, args=[], max_instances=1)

def kill(signal, frame):
    scheduler.shutdown(wait=False)
    cache.set("devices:kill-device", "all")
    sys.exit(0) 

def start():
    add_jobs()
    scheduler.start()
    cache.delete("devices:kill-device")

    
signal.signal(signal.SIGINT, kill)
signal.signal(signal.SIGTERM, kill)
