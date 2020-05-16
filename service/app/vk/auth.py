import os
import vk_api

from service.app import config


session = vk_api.VkApi(
    config.vk_login,
    config.vk_password
)


def auth_vk(vk_login, vk_password):
    os.environ['session_state'] = 'inactive'
    try:
        session.auth(token_only=True)
        print('new auth')
    except vk_api.AuthError:
        print('Ошибка аутентификации')
    os.environ['session_state'] = 'active'


def get_api():
    session_state = os.environ.get('session_state', 'inactive')
    if session_state == 'inactive':
        auth_vk(config.vk_login, config.vk_password)
    return session.get_api()
