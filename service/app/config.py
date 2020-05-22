import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    APP_NAME = os.getenv('APP_NAME', 'bot')

    VK_LOGIN = os.getenv('VK_LOGIN')
    VK_PASSWORD = os.getenv('VK_PASSWORD')

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    WORKER_SLEEP_TIME_SECONDS_DEFAULT = 60 * 60 * 24 * 3
    WORKER_SLEEP_TIME_SECONDS = int(os.getenv('WORKER_SLEEP_TIME_SECONDS', WORKER_SLEEP_TIME_SECONDS_DEFAULT))

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    USE_LOGGING = bool(os.getenv('USE_LOGGING', 'TRUE'))


config = Config()
