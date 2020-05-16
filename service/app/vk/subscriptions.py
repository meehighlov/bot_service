from service.app.vk.auth import get_api


def get_unsubscribed_users_info(query: str = None):
    api = get_api()
    subs = api.friends.getRequests(out=1)
    return subs[query] if query is not None else subs


def drop_all_friends_request():
    api = get_api()
    subs = get_unsubscribed_users_info()

    delete_result = [
        api.friends.delete(user_id=user_id)
        for user_id in subs['items']
    ]

    return delete_result
