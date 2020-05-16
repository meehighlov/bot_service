from service.api.v1.blueprint import v1_blueprint
from flask import jsonify

from service.app.vk.subscriptions import get_unsubscribed_users_info


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@v1_blueprint.route('/unsub/count', methods=['GET'])
def unsubscribed_users_count():
    return jsonify({'count': get_unsubscribed_users_info('count')})


@v1_blueprint.route('/unsub/ids', methods=['GET'])
def unsubscribed_user_ids():
    return jsonify({'ids': get_unsubscribed_users_info('items')})
