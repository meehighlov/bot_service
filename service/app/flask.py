import flask

from service.api import v1
from service.app import logging
from service.app.celery import init_celery
from service.app.config import config


def create_app():
    if config.USE_LOGGING:
        logging.init_logging()

    app = flask.Flask(__name__)
    app.config.from_object(config)

    init_celery(app)
    app.url_map.strict_slashes = False
    app.register_blueprint(v1.blueprint, url_prefix='/v1')

    return app
