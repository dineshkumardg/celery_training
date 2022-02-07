from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery_redis_project.celery import app

@shared_task
def testing():
    print('shared task is called')
    return 1

@shared_task
# @app.task
def add(x, y):
    testing.apply_async()
    return x + y