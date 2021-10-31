from flask import render_template, request, redirect, url_for
from . import main
from ..models import Review
from .forms import ReviewForm
from .forms import ReviewForm
from ..request import get_movies, get_movie,search_movie
# from app import app


Review = Review

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('main.search', movie_name = search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_playing = now_showing_movies)


@main.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    return render_template('movie.html', title = title, movie = movie, id = id, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    # title = f'Search results for {movie.name}'
    return render_template('search.html', movies = searched_movies)

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, review)
        new_review.save_review()
        return redirect(url_for('main.movie',id = movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title = title, review_form=form, movie = movie)

