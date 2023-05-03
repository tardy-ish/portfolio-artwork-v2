import os
import json
class Config(object):
    DEBUG = False
    TESTING = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    fp = json.load(open('./env.variables.json'))
    MAIL_USERNAME = fp['EMAIL']
    MAIL_PASSWORD = fp['MAIL_PASS']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True