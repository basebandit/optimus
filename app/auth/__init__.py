from flask import Blueprint
from app import oauth

auth = Blueprint('auth', __name__)
twitter = oauth.remote_app(
    'twitter',
    consumer_key='Usc8t6O4zr9tabNWFLRFojbnW',
    consumer_secret='9ieVATa7Jb1Wcl19ba8uzT4Q9jrBs8B8M769uruqc0mLPXruRf',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

from app.auth import views
