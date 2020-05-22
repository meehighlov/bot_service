import vk_api

from service.app.config import config


def auth_vk(session):
    try:
        session.auth(token_only=True)
    except vk_api.AuthError:
        # log it or something
        raise


def get_api():
    session = vk_api.VkApi(
        config.VK_LOGIN,
        config.VK_PASSWORD
    )
    auth_vk(session)
    return session.get_api()
