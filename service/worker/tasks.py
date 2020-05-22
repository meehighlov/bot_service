from service.app.celery import app
from service.app.vk.subscriptions import drop_all_friends_request


@app.task
def unlink_unsubscribed_users_task():
    drop_all_friends_request()
