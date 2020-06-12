import json
import os

import requests

from service.app.exceptions import WrongParametersFormatError


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


def on_start():
    return {
        'message': 'Enter two space separated names: first_name second_name',
        'keyboard': json.dumps({'buttons': [], 'one_time': True})
    }


def love_calculator_context_handler(request_data):

    peer_id = request_data['object']['message']['from_id']

    func_params = request_data['object']['message']['text']

    try:
        params = pre_process_data(func_params)
    except WrongParametersFormatError:
        return on_start()

    params = {
        'fname': params['fname'],
        'sname': params['sname']
    }

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "b9719c2e03mshd73af3a9902256bp1117b7jsn39bc6df975c6"
    }

    r = requests.get(
        'https://love-calculator.p.rapidapi.com/getPercentage',
        params=params,
        headers=headers
    )

    data = r.json()

    message = (
        f'% for {data["fname"]} and {data["sname"]} is {data["percentage"]}, {data["result"]}'
    )

    os.environ.pop(f'{peer_id}_next_func', None)

    return {
        'message': message,
        'keyboard': json.dumps(start_keyboard())
    }


def pre_process_data(data: str = None):
    if data is None:
        return {}
    try:
        first_name, second_name = data.split()
    except ValueError:
        raise WrongParametersFormatError
    return {
        'fname': first_name,
        'sname': second_name
    }


def love_calculator_scenario(request_data):
    peer_id = request_data['object']['message']['from_id']

    os.environ[f'{peer_id}_next_func'] = 'love_calculator_context_handler'

    return on_start()
