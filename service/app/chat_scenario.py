import json

from service.app.vk.utils import get_random_id


class CommonChat:

    mocked_response = 'I got you, but now i\'m busy holding my thoughts together'

    def _keyboard(self):
        return json.dumps([])

    def get_answer(self, data):
        return {
            'message': self.mocked_response,
            'peer_id': data['object']['message']['from_id'],
            'keyboard': self._keyboard(),
            'random_id': get_random_id()
        }


class LoveCalculator:

    def get_answer(self):
        return {
            'message': 'Введите два имени через пробел: Имя1 Имя2',
            'keyboard': {'buttons': [], 'one_time': True}
        }


def create_button(**kwargs):
    color = {'color': kwargs.pop('color')} if 'color' in kwargs else {}

    action = {
        attr: value
        for attr, value in kwargs.items()
    }

    return {
        **action,
        **color
    }


def keyboard():
    return {
        "one_time": False,
        'inline': False,
        "buttons": [
            [
                create_button(
                    type='text',
                    payload="{\"scenario\": \"1\"}",
                    label='Love calculator'
                )
            ]
        ]
    }


def get_answer(request_data: dict):
    response_data = {
        'peer_id': request_data['object']['message']['from_id'],
        'random_id': get_random_id()
    }

    payload = request_data.get('payload')

    if payload is None:
        pass

    scenario_number = payload['button']

    scenario = {
        '1': LoveCalculator
    }.get(scenario_number)

    response_data.update(
        scenario().get_answer()
    )

    # TODO handle dialog context!

    return response_data
