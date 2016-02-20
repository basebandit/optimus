import os

# WTF_CSRF_ENABLED = True

basedir = os.path.abspath(os.path.dirname(__file__))

# required by the Flask-SQLAlchemy extension.

SECRET_KEY = 'my_secret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'optimus.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
BCRYPT_LOG_ROUNDS = 13