import os
from celery import Celery

import accounts

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Create a Celery instance and set the broker and result backend.
app = Celery('backend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'accounts.tasks.test',
#         'schedule': 10,
#     },
#     'add-every-10-seconds': {
#         'task': 'accounts.tasks.test',
#         'schedule': 20,
#     },
#     'add-every-300-seconds': {
#         'task': 'accounts.tasks.test',
#         'schedule': 30.0,
#     },
# }


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')