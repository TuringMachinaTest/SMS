import time
from apscheduler.schedulers.background import BackgroundScheduler

from .tasks import event_listener

    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(event_listener, 'interval', seconds=10, args=[0], max_instances=1)
    scheduler.start()