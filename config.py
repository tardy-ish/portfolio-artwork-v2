import os
import json
class Config(object):
    DEBUG = False
    TESTING = False

    MAIL_SERVER = os.environ.get('SMTP_SERVER')
    MAIL_PORT = os.environ.get('SMTP_PORT')
    MAIL_USERNAME = os.environ.get('UNAME')
    MAIL_PASSWORD = os.environ.get('PASS')
    MAIL_USE_SSL = True if os.environ.get('SSL') == "True" else False
    MAIL_USE_TLS = True if os.environ.get('TLS') == "True" else False
    MAIL_DEFAULT_SENDER = os.environ.get('SENDER')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True