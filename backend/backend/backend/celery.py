from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

app = Celery('celeryapp')

app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0'
)

INTERVAL = 60.0

app.conf.beat_schedule = {
    'AAPL': {
        'task': 'api.tasks.fetch_stock_price',
        'schedule': INTERVAL,
        'kwargs': {'symbol': 'AAPL'}
    },
    'NVDA': {
        'task': 'api.tasks.fetch_stock_price',
        'schedule': INTERVAL,
        'kwargs': {'symbol': 'NVDA'}
    },
    'INTC': {
        'task': 'api.tasks.fetch_stock_price',
        'schedule': INTERVAL,
        'kwargs': {'symbol': 'INTC'}
    },
    'BTC': {
        'task': 'api.tasks.fetch_crypto_price',
        'schedule': INTERVAL,
        'kwargs': {'symbol': 'BTC'}
    },
    'ETH': {
        'task': 'api.tasks.fetch_crypto_price',
        'schedule': INTERVAL,
        'kwargs': {'symbol': 'ETH'}
    }
}

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.timezone = settings.TIME_ZONE
app.conf.enable_utc = False

if __name__ == '__main__':
    app.start(['beat'])
