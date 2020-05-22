from service.app.flask import create_app  # noqa F401

flask_app = create_app()

from service.app.celery import app  # noqa F401
