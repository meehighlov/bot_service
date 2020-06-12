import json

from service.app.commands import execute_command
from service.app.exceptions import CommandError, ExternalServiceCallError, BaseError
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
                    label='кнопуля пока не робит',
                    color='positive'
                )
            ]
        ]
    }


def get_answer(request_data: dict):
    peer_id = request_data['object']['message']['from_id']
    response_data = {
        'message': 'mocked message',
        'keyboard': json.dumps(start_keyboard()),
        'peer_id': peer_id,
        'random_id': get_random_id()
    }

    message_text = request_data['object']['message']['text']

    try:
        message = execute_command(message_text)
    except CommandError as ce:
        message = f'Error during command execution - {ce.context}'
    except ExternalServiceCallError as esce:
        message = f'Service {esce.context} not available'
    except BaseError as be:
        print(be)
        message = f'Something strange happen'
    except Exception as e:
        print(e)
        message = f'WOW, something really goes bad'

    response_data.update({'message': message})

    return response_data
