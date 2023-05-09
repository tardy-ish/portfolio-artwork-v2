import os
import json
class Config(object):
    DEBUG = False
    TESTING = False

    MAIL_SERVER = os.environ.get('SMTP_SERVER').strip()
    MAIL_PORT = os.environ.get('SMTP_PORT').strip()
    MAIL_USERNAME = os.environ.get('UNAME').strip()
    MAIL_PASSWORD = os.environ.get('PASS').strip()
    MAIL_USE_SSL = True if os.environ.get('SSL').strip() == "True" else False
    MAIL_USE_TLS = True if os.environ.get('TLS').strip() == "True" else False
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL').strip()

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True