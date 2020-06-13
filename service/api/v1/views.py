from service.api.serializers.vk_call_back_event import VKChatSchema, VKGroupJoinSchema, VKEventSchema
from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config
from service.app.chat_handler import get_answer, group_join_answer
from service.app.vk.client import call


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    print('json in request', request.get_json())

    event = VKEventSchema().load(request.get_json())

    if event['type'] == 'confirmation':
        return config.CONFIRMATION_CODE

    if event['type'] == 'group_join':
        join_group_data = VKGroupJoinSchema().load(request.get_json())
        params = group_join_answer(join_group_data)
        call('messages.send', params=params)

    if event['type'] == 'message_new':
        data = VKChatSchema().load(request.get_json())
        params = get_answer(data)
        call('messages.send', params=params)

    return 'ok'
