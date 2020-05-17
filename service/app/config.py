import os

from dotenv import load_dotenv


load_dotenv(verbose=True)


class Config:
    VK_LOGIN = os.getenv('VK_LOGIN')
    VK_PASSWORD = os.getenv('VK_PASSWORD')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    WORKER_SLEEP_TIME_SECONDS = os.getenv('WORKER_SLEEP_TIME_SECONDS')


config = Config()
