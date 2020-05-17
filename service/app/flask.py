import flask

from service.api import v1
from service.app.celery import init_celery
from service.app.config import config


def create_app():

    app = flask.Flask(__name__)
    app.config.from_object(config)

    init_celery(app)

    app.url_map.strict_slashes = False
    app.register_blueprint(v1.blueprint, url_prefix='/v1')

    return app
