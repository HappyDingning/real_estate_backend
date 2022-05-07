import os
from django.conf import settings

from celery import Celery
from celery.beat import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_backend.settings')

app = Celery('ether_events_moniter', 
             broker='redis://172.30.226.45:6379/1',
             backend='redis://172.30.226.45:6379/2',
             broker_connection_retry_on_startup=True)

app.conf.beat_schedule = {
    'ethereum_events': {
        'task': 'django_ethereum_events.tasks.event_listener',
        'schedule': crontab(minute='*/1')  # run every minute
    }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
