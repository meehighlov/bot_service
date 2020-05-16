from service.app.vk.auth import get_api


def get_count_unsubscribed_users():
    api = get_api()
    subs = api.users.getSubscriptions()
    return subs['users']['count']


def get_unsubscribed_user_ids():
    api = get_api()
    subs = api.users.getSubscriptions()
    return subs['users']['items']
