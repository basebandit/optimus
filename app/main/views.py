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
    # return render_template('index.html', project=project, name=name)
    return render_template('.html')


# accepts GET and  POST requests.
@app.route('/login', methods=['POST'])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
    by processing the form."""

    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(user.password, json_data['password']):
        session['logged_in'] = True
        status = True
    else:
        status = False
    return jsonify({'result': status})


@app.route('/register', methods=['POST'])
def register():
    json_data = request.json
    user = User(email=json_data['email'],
                password=json_data['password'])
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
    except:
        status = 'this user is already registered'
    db.session.close()
    return jsonify({'result': status})


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})
