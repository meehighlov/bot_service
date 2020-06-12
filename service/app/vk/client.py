import requests

from service.app.config import config


def call(method, params):
    params_ = {
        'access_token': config.BOT_TOKEN,
        'v': config.VK_API_VERSION
    }

    params_.update(**params)

    try:
        print('request params:', params_)
        r = requests.get(f'{config.VK_API_URL}{method}', params=params_)
        print('response:', r.json())
    except Exception as e:
        r = {'error': 1}
        print(e)  # TODO log
    return r
