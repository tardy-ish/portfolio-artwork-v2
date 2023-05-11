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

    db_user = os.getenv('db_u').strip()
    db_pass = os.getenv('db_p').strip()
    db_host = os.getenv('db_h').strip()
    db_name = os.getenv('db_n').strip()
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_user}:{db_pass}@{db_host}/{db_name}'



class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True