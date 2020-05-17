import vk_api

from service.app.config import config


session = vk_api.VkApi(
    config.VK_LOGIN,
    config.VK_PASSWORD
)


def auth_vk():
    try:
        session.auth(token_only=True)
        print('new auth')
    except vk_api.AuthError:
        print('Ошибка аутентификации')
        raise


def get_api():
    auth_vk()
    return session.get_api()
