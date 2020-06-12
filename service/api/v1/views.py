from service.api.serializers.vk_call_back_event import VKChatSchema
from service.api.v1.blueprint import v1_blueprint
from flask import jsonify
from flask import request

from service.app.config import config
from service.app.chat_scenario import get_answer
from service.app.vk.client import call


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/chat', methods=['POST'])
def chat_view():
    data = VKChatSchema().load(request.get_json())

    if data['type'] == 'message_reply':
        return 'ok'

    if data['type'] == 'confirmation':
        # params = {
        #     'access_token': config.BOT_TOKEN,
        #     'group_id': config.GROUP_ID,
        #     'v': config.VK_API_VERSION
        # }
        #
        # confirmation_code_response = requests.get(
        #     f'{config.VK_API_URL}groups.getCallbackConfirmationCode',
        #     params=params,
        # )
        #
        # print(confirmation_code_response.json())
        #
        # confirmation_code = confirmation_code_response.json()['response']['code']
        return config.CONFIRMATION_CODE

    print('request_data', data)
    params = get_answer(data)
    print('params', params)

    call('messages.send', params=params)

    return 'ok'
