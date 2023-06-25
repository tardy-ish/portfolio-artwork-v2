import os
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

class Config(object):
    DEBUG = False
    TESTING = False

    # MAIL_SERVER = os.getenv('SMTP_SERVER').strip()
    # MAIL_PORT = os.getenv('SMTP_PORT').strip()
    # MAIL_USERNAME = os.getenv('UNAME').strip()
    # MAIL_PASSWORD = os.getenv('PASS').strip()
    # MAIL_USE_SSL = True if os.getenv('SSL').strip() == "True" else False
    # MAIL_USE_TLS = True if os.getenv('TLS').strip() == "True" else False
    # MAIL_DEFAULT_SENDER = os.getenv('EMAIL').strip()

    db_user = os.getenv('DB_USERNAME').strip()
    db_pass = os.getenv('DB_PASS').strip()
    db_host = os.getenv('DB_HOST').strip()
    db_name = os.getenv('DB_NAME').strip()
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}'



class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True