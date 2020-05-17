import os
import vk_api

from service.app.config import config


session = vk_api.VkApi(
    config.VK_LOGIN,
    config.VK_PASSWORD
)


def auth_vk():
    os.environ['session_state'] = 'inactive'
    try:
        session.auth(token_only=True)
        print('new auth')
    except vk_api.AuthError:
        print('Ошибка аутентификации')
        raise
    os.environ['session_state'] = 'active'


def get_api():
    session_state = os.environ.get('session_state', 'inactive')
    if session_state == 'inactive':
        auth_vk()
    return session.get_api()
