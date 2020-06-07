import requests

from service.api.serializers.vk_call_back_event import VKChat
from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config
from service.app.vk.chat_scenario import get_answer


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    data = VKChat().load(request.get_json())

    if data['type'] == 'confirmation':
        return config.CONFIRMATION_CODE

    params = get_answer(data)
    requests.get(f'{config.VK_API_URL}messages.send', params=params)

    return 'ok'
