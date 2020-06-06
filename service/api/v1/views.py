import json

import requests

from service.api.serializers.vk_call_back_event import VKCallBackAPIEvent
from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config
from service.app.vk.chat_scenario import get_answer
from service.app.vk.utils import get_random_id


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    data = VKCallBackAPIEvent().load(request.get_json())

    if data['type'] == 'confirmation':
        return config.CONFIRMATION_CODE

    if data['type'] == 'message_new':

        if 'payload' in data['object']['message']:
            payload = json.loads(data['object']['message']['payload'])
            command = payload.get('command')
            if command == 'start':
                pass  # TODO new user triggered the bot event

        user_sender_id = data['object']['message']['from_id']

        response, keyboard = get_answer(data)

        # print('response', response)
        # print('keyboard', keyboard)
        print('data', data)

        response_data = {
            'message': response,
            'keyboard': json.dumps(keyboard),
            'peer_id': user_sender_id,
            'access_token': config.BOT_TOKEN,
            'v': config.VK_API_VERSION,
            'random_id': get_random_id()
        }

        r = requests.get(f'{config.VK_API_URL}messages.send', params=response_data)

        print(r.json())

    return 'ok'
