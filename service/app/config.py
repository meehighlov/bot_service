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

    X_RAPIDAPI_HOST = os.getenv('X_RAPIDAPI_HOST')
    X_RAPIDAPI_KEY = os.getenv('X_RAPIDAPI_KEY')


config = Config()
