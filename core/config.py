import logging
from dotenv import load_dotenv, find_dotenv
import os
from datetime import timedelta


class Config(object):
    
    def __init__(self):
        load_dotenv(find_dotenv('.env'))
        self.DEBUG = True
        self.TESTING = False
        self.PRODUCTION = False
        self.APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        self.AUTHENTICATION_SOURCE = '',

        self.ERROR_INCLUDE_MESSAGE = False

        # os.getenv("JWT_ACCESS_CSRF_HEADER_NAME")

        self.LOG_LEVEL = logging.DEBUG

        AUTHENTICATION_SOURCE = '',
        try:
            # Python 3.x
            from urllib.parse import quote_plus
        except ImportError:
            # Python 2.x
            from urllib import quote_plus

    @staticmethod
    def mongo_from_uri(uri):
        print(uri)
        conn_settings = {"host": uri}
        return conn_settings


class Development(Config):
    """
        Use "if app.debug" anywhere in your code,
        that code will run in development mode.
    """

    def __init__(self):
        super(Development, self).__init__()
        self.ENVIRONMENT = "Dev"
        self.DEBUG = True
        self.TESTING = False


class Production(Config):
    def __init__(self):
        super(Development, self).__init__()
        self.ENVIRONMENT = "Prod"
        self.DEBUG = False
        self.TESTING = False


class TestingConfig(Config):
    DEBUG = True
    try:
        # Python 3.x
        from urllib.parse import quote_plus
    except ImportError:
        # Python 2.x
        from urllib import quote_plus



config_by_name = dict(
    dev=Development,
    test=TestingConfig,
    prod=Production
)
