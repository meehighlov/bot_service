import requests

from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config
from service.app.vk.chat_scenario import get_answer
from service.app.vk.users import get_user_by_id


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    data = request.get_json()

    print(data)

    if data['type'] == 'confirmation':
        return config.CONFIRMATION_CODE

    if data['type'] == 'message_new':
        user_sender_id = data['object']['message']['from_id']

        # user_sender_data = get_user_by_id(user_sender_id)
        # print(user_sender_data)

        response = get_answer(data)

        response_data = {
            'message': response,
            'peer_id': user_sender_id,
            'access_token': config.BOT_TOKEN,
            'v': config.VK_API_VERSION,
            'random_id': '0'
        }

        r = requests.get('https://api.vk.com/method/messages.send', params=response_data)

    return 'ok'
