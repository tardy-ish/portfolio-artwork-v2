import os
import json
class Config(object):
    DEBUG = False
    TESTING = False

    MAIL_SERVER = os.getenv('SMTP_SERVER').strip()
    MAIL_PORT = os.getenv('SMTP_PORT').strip()
    MAIL_USERNAME = os.getenv('UNAME').strip()
    MAIL_PASSWORD = os.getenv('PASS').strip()
    MAIL_USE_SSL = True if os.getenv('SSL').strip() == "True" else False
    MAIL_USE_TLS = True if os.getenv('TLS').strip() == "True" else False
    MAIL_DEFAULT_SENDER = os.getenv('EMAIL').strip()

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True