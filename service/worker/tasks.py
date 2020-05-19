from service.app.celery import app


@app.task
def unlink_unsubscribed_users_task():
    with open('file.txt') as f:
        f.write('task is done')
