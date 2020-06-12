from service.api.serializers.vk_call_back_event import VKChatSchema
from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config
from service.app.chat_handler import get_answer
from service.app.vk.client import call


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    print('json in request', request.get_json())
    data = VKChatSchema().load(request.get_json())

    if data['type'] == 'message_reply':
        return 'ok'

    if data['type'] == 'confirmation':
        return config.CONFIRMATION_CODE

    params = get_answer(data)

    call('messages.send', params=params)

    return 'ok'
