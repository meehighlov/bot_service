import json
import os

from service.app.bot_options.love_calculator import love_calculator_scenario, love_calculator_context_handler
from service.app.exceptions import ContextError
from service.app.vk.utils import get_random_id


def create_button(**kwargs):
    color = {'color': kwargs.pop('color')} if 'color' in kwargs else {}

    action = {
        attr: value
        for attr, value in kwargs.items()
    }

    return {
        'action': action,
        **color
    }


def start_keyboard():
    return {
        "one_time": False,
        'inline': False,
        "buttons": [
            [
                create_button(
                    type='text',
                    payload="{\"button\": \"1\"}",
                    label='Love calculator',
                    color='primary'
                )
            ]
        ]
    }


def get_context_handler(func_name):
    try:
        func = {
            'love_calculator_context_handler': love_calculator_context_handler
        }[func_name]
    except KeyError:
        raise ContextError
    return func


def get_answer(request_data: dict):
    peer_id = request_data['object']['message']['from_id']
    response_data = {
        'message': 'mocked message',
        'keyboard': json.dumps(start_keyboard()),
        'peer_id': peer_id,
        'random_id': get_random_id()
    }

    context = os.getenv(f'{peer_id}_next_func')

    if context:
        func = get_context_handler(context)
        response = func(request_data)

        response_data.update(**response)
        return response_data

    button = None

    if 'payload' in request_data['object']['message']:
        payload = request_data['object']['message']['payload']
        button = payload['button']

    scenario = {
        '1': love_calculator_scenario
    }.get(button)

    if scenario:
        response = scenario(request_data)
        response_data.update(**response)

    return response_data
