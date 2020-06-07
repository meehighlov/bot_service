import json

from service.app.config import config
from service.app.vk.utils import get_random_id


def create_button(**kwargs):
    return {
        'action': {
            attr: value
            for attr, value in kwargs.items()
        },
        'color': kwargs.get('color')
    }


def keyboard():
    return {
        "one_time": False,
        "buttons": [
            [
                create_button(
                    type='text',
                    payload="{'button': '2'}",
                    label='wow',
                    color='secondary'
                )
            ],
            [
                create_button(
                    type='text',
                    payload="{'button': '1'}",
                    label='hey',
                    color='positive'
                ),
                create_button(
                    type='text',
                    payload="{'button': '0'}",
                    label='path',
                    color='negative'
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
        'v': config.VK_API_VERSION,
        'random_id': get_random_id()
    }

    if 'payload' in request_data['object']['message']:
        response_data.update({
            'keyboard': json.dumps(keyboard())
        })

    return response_data
