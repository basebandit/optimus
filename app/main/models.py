from app import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager


class User(UserMixin, db.Model):
    """An admin user capable of viewing reports.

       :param str email: email address of user
       :param str password: encrypted password for the user

       """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    registered_on = db.Column(db.DATETIME, nullable=False)

    @property
    def password(self, password):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        """Returns a string representation of the User object."""
        return '<User {0}'.format(self.email)


class Movie(db.Model):
    """A movie for sale on our site.

    :param int id: Unique id for this movie
    :param str name: Human-readable name of this movie
    :param str file_name: Path to file this  movie represents
    :param str version: Optional version to track updates to movies
    :param bool is_active: Used to denote if a movie should be considered for-sale
    :param float price: Price of movie
        """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, default=None, nullable=False)
    releaseYear = db.Column(db.Integer, default="Year unknown")
    director = db.Column(db.String, default="Unknown director")
    genre = db.Column(db.String, default=None, nullable=True)
    availability = db.Column(db.Integer, default=None, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    """receives a user identifier as a Unicode string"""
    return User.query.get(int(user_id))
