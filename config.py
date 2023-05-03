import os
class Config(object):
    DEBUG = False
    TESTING = False

    # MAIL_SERVER = 'smtpout.secureserver.net'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'hello@lanakhayat.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'hello@lanakhayat.com'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True