import os
class Config(object):
    DEBUG = False
    TESTING = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('EMAIL')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True