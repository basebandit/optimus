import os

# WTF_CSRF_ENABLED = True

basedir = os.path.abspath(os.path.dirname(__file__))


# required by the Flask-SQLAlchemy extension.

class Config:
    SECRET_KEY = 'my_secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'optimus.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    OPTIMUS_MAIL_SUBJECT_PREFIX = '[Optimus]'
    OPTIMUS_MAIL_SENDER = 'Optimus Admin <evansonmwangi83@gmail.com>'
    OPTIMUS_ADMIN = os.environ.get('OPTIMUS_ADMIN')
    TEST_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'test_optimus.sqlite')
    DEV_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'dev_optimus.sqlite')
    PROD_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'prod_optimus.sqlite')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DEV_DATABASE_URL
    


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = Config.TEST_DATABASE_URL


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = Config.PROD_DATABASE_URL


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
