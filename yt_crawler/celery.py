from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt_crawler.settings')
app = Celery('yt_crawler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
    'crawl-every-300-seconds': {
        'task': 'api.tasks.yt_crawl_job', 
        'schedule': 300.0, # Repeats fetching in 300 seconds
    },
}
app.autodiscover_tasks() #look up for tasks.py file in all the apps