import logging.config

from service.app.config import config


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': (
                '%(levelname)s %(asctime)s %(name)s %(funcName)s %(request_id)s %(message)s'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': config.LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': config.LOG_LEVEL,
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'stream': 'bot.log'
        }
    },
    'loggers': {
        config.APP_NAME: {
            'level': config.LOG_LEVEL,
            'handlers': ['file', 'console'],
        },
    }
}


def init_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
