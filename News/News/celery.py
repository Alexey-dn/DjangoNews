import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News.settings')

app = Celery('News')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_morning': {
        'task': 'chitchat.tasks.new_post_notification',
        'schedule': crontab(minute="0",  hour="18", day_of_week="fri")
        # 'schedule': 30,
    },
}
