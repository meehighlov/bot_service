from service.api.v1.blueprint import v1_blueprint
from flask import jsonify


@v1_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})
