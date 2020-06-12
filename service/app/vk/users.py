from service.api.serializers.vk_user import VKUsersSchema
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

    response = call(method='users.get', params=params)

    data = VKUsersSchema().load(response.json())
    return data['response'][0]
