import os


class BaseConfig(object):
    DEBUG = bool(int(os.getenv('FLASK_DEBUG', '0')))
    TESTING = bool(int(os.getenv('FLASK_TESTING', '0')))
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

    LOG_FOLDER = os.getenv('FLASK_LOG_FOLDER', '')


    FLASK_ROOT_PATH = os.getenv('FLASK_ROOT_PATH')
