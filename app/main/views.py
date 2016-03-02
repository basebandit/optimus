from flask import render_template
from ..models import Movie
from random import randint
from . import main


@main.route('/')
def index():
    movies = Movie.query.order_by(Movie.id).all()
    _random = randint(1, 13)
    image_file = "images/" + str(_random) + ".jpg"
    print image_file
    return render_template('index.html', image=image_file, movies=movies)
