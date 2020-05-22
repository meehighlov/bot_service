from service.app.vk.auth import get_api


def drop_all_friends_request():
    api = get_api()
    subs = api.friends.getRequests(out=1)

    delete_result = [
        api.friends.delete(user_id=user_id)
        for user_id in subs['items']
    ]

    return delete_result
