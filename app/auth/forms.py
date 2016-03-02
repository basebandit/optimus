from flask.ext.wtf import Form
from wtforms import ValidationError
from app.models import User, Movie
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class SignupForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                     'Usernames must have only letters, '
                                                                                     'numbers, dots or underscores')])
    password = PasswordField('Password',
                             validators=[Required(), EqualTo('confirm_password', message='Passwords must match.')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Create Account')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    password = PasswordField('New Password',
                             validators=[Required(), EqualTo('confirm_password', message='Passwords did not match.')])
    confirm_password = PasswordField('Confirm New Password', validators=[Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError("Unknown email address.")


class AddMovieForm(Form):
    title = StringField('Title', validators=[Required()])
    genre = StringField('Genre', validators=[Required()])
    review = TextAreaField('Synopsis', validators=[Required()])
    release_year = IntegerField('Release_Year', validators=[Required()])
    director = StringField('Director', validators=[Required()])
    availability = IntegerField('Availability', validators=[Required()])
    submit = SubmitField('Add')

    def get_movie_by_title(self, field):
        if Movie.query.filter_by(title=field.data).first() is None:
            raise ValidationError("No such Movie")
        else:
            return "Movie already in store."


class EditMovieForm(Form):
    title = StringField('Title', validators=[Required()])
    genre = StringField('Genre', validators=[Required()])
    review = TextAreaField('Synopsis', validators=[Required()])
    release_year = IntegerField('Release_Year', validators=[Required()])
    director = StringField('Director', validators=[Required()])
    availability = IntegerField('Availability', validators=[Required()])
    submit = SubmitField('Edit')
