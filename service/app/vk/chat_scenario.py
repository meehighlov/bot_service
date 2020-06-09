import json

from service.app.config import config
from service.app.vk.utils import get_random_id


def create_button(**kwargs):
    return {
        'action': {
            attr: value
            for attr, value in kwargs.items()
            if attr != 'color'
        },
        'color': kwargs.get('color')
    }


def keyboard():
    return {
        "one_time": False,
        "buttons": [
            [
                create_button(
                    type='location',
                    payload="{\"button\": \"1\"}",
                )
            ],
            [
                create_button(
                    type='text',
                    payload="{\"button\": \"2\"}",
                    label='нет, нойс',
                    color='positive'
                ),
                create_button(
                    type='text',
                    payload="{\"button\": \"3\"}",
                    label='да, нойс',
                    color='positive'
                )
            ]
        ]
    }


def get_answer(request_data: dict):
    response = 'mocked message'  # temporary stub for any message

    response_data = {
        'message': response,
        'peer_id': request_data['object']['message']['from_id'],
        'access_token': config.BOT_TOKEN,
        'keyboard': json.dumps(keyboard()),
        'v': config.VK_API_VERSION,
        'random_id': get_random_id()
    }

    return response_data
