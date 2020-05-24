from service.api.v1.blueprint import v1_blueprint
from flask import jsonify, request

from vk_api.utils import get_random_id

from service.app.vk.auth import session_factory_with_auth


session = session_factory_with_auth(
    token=''
)


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/vk_request_handler', methods=['POST'])
def vk_handler():
    api = session().get_api()

    data = request.get_json()

    if not data or 'type' not in data:
        return 400

    if data['type'] == 'confirmation':
        return '42a82a6f'
    elif data['type'] == 'message_new':
        print(data)
        from_id = data['object']['message']['from_id']
        # отправляем сообщение
        api.messages.send(
            message='stub message',
            random_id=get_random_id(),
            peer_id=from_id
        )
        return 200
