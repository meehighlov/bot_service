import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    APP_NAME = os.getenv('APP_NAME', 'bot')

    VK_API_URL = os.getenv('VK_API_URL')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CONFIRMATION_CODE = os.getenv('CONFIRMATION_CODE')
    GROUP_ID = os.getenv('GROUP_ID')
    SECRET_CODE = os.getenv('SECRET_CODE')
    VK_API_VERSION = os.getenv('VK_API_VERSION')
    MY_VK_ID = os.getenv('MY_VK_ID')

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    WORKER_SLEEP_TIME_SECONDS_DEFAULT = 60 * 60 * 24 * 3  # three days
    WORKER_SLEEP_TIME_SECONDS = int(os.getenv('WORKER_SLEEP_TIME_SECONDS', WORKER_SLEEP_TIME_SECONDS_DEFAULT))


config = Config()
