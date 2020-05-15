import flask

from service.api import v1


def create_app():

    app = flask.Flask(__name__)

    app.url_map.strict_slashes = False
    app.register_blueprint(v1.blueprint, url_prefix='/v1')

    return app
