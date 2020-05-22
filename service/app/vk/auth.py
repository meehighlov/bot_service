import vk_api

import logging
from service.app.config import config

logger = logging.getLogger(config.APP_NAME)


def auth_vk(session):
    try:
        session.auth(token_only=True)
    except vk_api.AuthError as ve:
        logger.error(ve)
        raise


def get_api():
    session = vk_api.VkApi(
        config.VK_LOGIN,
        config.VK_PASSWORD
    )
    auth_vk(session)
    return session.get_api()
