import celery

from service.app.config import config

app = celery.Celery(
    'celery',
    broker=config.CELERY_BROKER_URL,
    include=[
        'service.worker',
    ]
)

app.conf.beat_schedule = {
    'unlink_unsubscribed_users': {
        'task': 'service.worker.tasks.unlink_unsubscribed_users_task',
        'schedule': config.WORKER_SLEEP_TIME_SECONDS
    }
}


def init_celery(flask_app):
    class ContextTask(app.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    app.Task = ContextTask
