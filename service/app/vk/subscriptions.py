from service.app.vk.auth import get_api


def get_unsubscribed_users_info(query: str):
    api = get_api()
    subs = api.users.getSubscriptions()
    return subs['users'][query]
