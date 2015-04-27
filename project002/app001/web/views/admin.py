from flask import Blueprint, request, jsonify
from werkzeug.datastructures import MultiDict
from app001.web.forms.admin import NewMovieForm
from app001.web.models.admin import Admin


adminbp = Blueprint('adminbp', __name__, url_prefix='/admin')


@adminbp.route('/movie/add', methods=['POST'])
def add_movie():
    """Add new movies

    """
    form = NewMovieForm(MultiDict(request.json))

    if not form.validate():
        resp = jsonify()
        resp.status_code = 400
        return resp

    movie_id = Admin(movie_name=form.name.data).add_movie()
    return jsonify(movie_id=movie_id)


@adminbp.route('/movies', methods=['GET'])
def list_movies():
    """Returns a list of movies

    """
    movies = Admin.get_all_movies()

    return jsonify(movies=movies)
