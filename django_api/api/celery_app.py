import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()



app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'users.tasks.send_notify_users',
        'schedule': 10.0
    }
}
