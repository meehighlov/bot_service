import celery

from service.app.config import config

app = celery.Celery(
    'directions-itc',
    broker=config.CELERY_BROKER_URL,
    include=[
        'directions_itc.worker.tasks',
    ]
)
