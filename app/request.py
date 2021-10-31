# from app import app
import urllib.request,json

# from app.models.movie_test import Movie
from .models import Movie

Movie = Movie

api_key = None

base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_movies(category):
    '''
    get json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key)
    print(get_movies_url)
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

def process_results(movie_list):
    '''
    Transform movie results to a list of objects
    '''
    movie_result = []
    for item in movie_list:
        # print(item)
        id = item.get('id')
        title = item.get('title')
        overview = item.get('overview')
        poster = item.get('poster_path')
        vote_average = item.get('vote_average')
        vote_count = item.get('vote_count')


        if poster:
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            movie_result.append(movie_object)
    return movie_result

def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)

    return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results


          


