from service.api.serializers.vk_user import VKUsersSchema
from service.app.exceptions import ExternalServiceCallError
from service.app.vk.client import call
from service.app.vk.utils import get_random_id


def get_user_by_id(user_id):

    """
    Возвращает основную информацию о пользователе

    :param user_id: id пользователя VK
    :return:
    """

    user_id = str(user_id)
    params = {
        'user_id': user_id,
        'random_id': get_random_id(),
    }

    try:
        response = call(method='users.get', params=params)
    except Exception:
        raise ExternalServiceCallError(context='Fail on getting user data')

    data = VKUsersSchema().load(response.json())
    return data['response'][0]
