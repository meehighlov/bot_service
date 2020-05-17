from service.app.celery import app


@app.task
def check_unsubscribed_users_task():
    pass
