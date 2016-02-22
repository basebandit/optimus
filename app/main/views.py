from flask import render_template, flash, redirect, jsonify, request
from app import app
from app import bcrypt
from app import db
from flask.ext.login import session
from models import User


# maps to / in the url
@app.route('/')
# maps to /index in the url
@app.route('/index')
def index():
    project = "Optimus"
    name = "Devmars"
    return render_template('index.html')


# accepts GET and  POST requests.
@app.route('/login', methods=['GET', 'POST'])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
    by processing the form."""
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    return render_template('catalog.html')
