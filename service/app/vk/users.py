import requests

from service.api.serializers.vk_user import VKUserSchema
from service.app.config import config

url_tail = 'users.get'


def get_user_by_id(user_id):

    """
    Возвращает основную информацию о пользователе

    :param user_id: id пользователя VK
    :return:
    """

    user_id = str(user_id)
    params = {
        'user_id': user_id,
    }

    response = requests.get(f'{config.VK_API_URL}{url_tail}', params=params)

    return VKUserSchema().load(response.json()).data


def get_users(params: dict):
    pass
