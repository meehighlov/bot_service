from service.app.celery import app


@app.task
def unlink_unsubscribed_users_task():
    pass
