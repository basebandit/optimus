from random import randint
import re
from app import db
from app.auth import auth
from app.auth.forms import LoginForm, SignupForm, AddMovieForm, EditMovieForm
from app.models import User, Movie
from config import Config
from app.auth import twitter
from flask import render_template, redirect, request, url_for, flash, g
from flask.ext.login import login_user, logout_user, login_required, session, current_user
from sqlalchemy.sql import func


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('auth.dashboard'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/twitter-login')
def twitter_login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    callback_url = url_for('auth.oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)


@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # token = user.generate_confirmation_token()
        login_user(user, form.password.data)
        flash('You can now login.')
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('Please Login To Access The Dashboard.')
    return redirect(url_for('main.index'))

    if Config.TWITTER_LOGIN:
        session.pop('twitter_oauth', None)
        flash('You were signed out successfully!')
        return redirect(url_for('main.index'))
    else:
        logout_user()
        flash('You were signed out successfully!')
        return redirect(url_for('main.index'))


@auth.route('/movies/add', methods=['GET', 'POST'])
@login_required
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.title.data, genre=form.genre.data, review=form.review.data,
                      director=form.director.data, release_year=form.release_year.data,
                      availability=form.availability.data)
        db.session.add(movie)
        db.session.commit()
        return redirect(request.args.get('next') or url_for('auth.dashboard'))
    # flash('Movie added successfully!')
    return render_template('auth/add.html', form=form)


@auth.route('/oauthorized')
def oauthorized():
    resp = twitter.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
        redirect(url_for('main.index'))
    else:
        session['twitter_oauth'] = resp
    print resp['screen_name']
    this_user = User.query.filter_by(username=resp['screen_name']).first()
    if this_user is None:
        new_user = User(username=resp['screen_name'],
                        password=resp['oauth_token_secret'])
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
    else:
        login_user(this_user)
    return redirect(url_for('auth.dashboard'))


@auth.route('movies/delete')
@login_required
def delete_movie():
    pass


@auth.route('movies/edit')
@login_required
def edit_movie():
    form = EditMovieForm()


@auth.route('/dashboard')
@login_required
def dashboard():
    movies = Movie.query.order_by(Movie.id).all()
    _available = db.session.query(func.sum(Movie.availability)).all()
    available = re.sub('[^0-9]', '', str(_available))
    count = Movie.query.count()
    releases = randint(1, 50)
    views = randint(200, 10000)
    _danger = randint(0, 100)
    _warning = randint(0, 100)
    return render_template('auth/dashboard.html', _danger=_danger, _warning=_warning, movies=movies, count=count,
                           available=available, releases=releases, views=views)
