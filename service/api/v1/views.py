import requests

from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/info', methods=['GET'])
def info():
    pass


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    data = request.get_json()

    if data['type'] == 'confirmation':
        return config.CONFIRMATION_CODE

    if data['type'] == 'message_new':
        user_sender = data['object']['message']['from_id']

        response_data = {
            'message': 'stub message',
            'peer_id': user_sender,
            'access_token': config.BOT_TOKEN,
            'v': config.VK_API_VERSION,
            'random_id': '0'
        }

        r = requests.get('https://api.vk.com/method/messages.send', params=response_data)

    return 'ok'
