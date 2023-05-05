import os
import json
class Config(object):
    DEBUG = False
    TESTING = False

    MAIL_SERVER = os.environ.get('SMTP_SERVER')
    MAIL_PORT = os.environ.get('SMTP_PORT')
    MAIL_USERNAME = os.environ.get('EMAIL')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
    MAIL_USE_TLS = os.environ.get('TLS')
    MAIL_USE_SSL = os.environ.get('SSL')
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True