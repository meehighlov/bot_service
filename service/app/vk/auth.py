import vk_api

from service.app.config import config


def auth_vk(session):
    try:
        session.auth(token_only=True)
        print('new auth')
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


def session_factory_with_auth(vk_login=None, vk_password=None, token=None):
    # vk_session = vk_api.VkApi(
    #     vk_login,
    #     vk_password
    # ) if token is None else vk_api.VkApi(token=token)

    # auth_vk(vk_session)

    vk_session = vk_api.VkApi(token=token)

    def session_():
        return vk_session

    return session_
