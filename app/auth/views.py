from flask import render_template, jsonify, request, url_for, flash, redirect
from flask.ext.login import login_user
from . import auth
from app import app
from app import db
from .forms import LoginForm
from app.main.models import User


# accepts GET and  POST requests.
@app
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
    by processing the form."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template("auth/login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('auth/signup.html')


@app.route('/logout')
def logout():
    # session.pop('logged_in', None)
    return jsonify({'result': 'success'})


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    return render_template('catalog.html')
