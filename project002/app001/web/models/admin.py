from app001.utils.core import Transaction
from app001.utils.settings import DB_SESSION as db_session
from app001.utils.mappings import Movie


class Admin(object):

    """ This class provides administrative methods to manage movies

    """

    def __init__(self, movie_name=None):
        """Constructor

        :param movie_name: Movie Name
        :type movie_name: str

        """
        self.movie_name = movie_name

    def add_movie(self):
        """Add a new movie

        Required Constructor params:
        1. movie_name

        """
        if not self.movie_name:
            raise ValueError(
                'A valid movie_name constructor param is required')

        with Transaction() as t:
            movie = Movie(name=self.movie_name)
            t.add(movie)
            t.commit()
        return movie.id

    def movie_exists(self):
        """This method checks if the movie already exists in the db

        Required Constructor params:
        1. movie_name

        """
        if not self.movie_name:
            raise ValueError(
                'A valid movie_name constructor param is required')

        return bool(db_session.query(Movie.id
                                     ).filter(Movie.name == self.movie_name
                                              ).count())

    @classmethod
    def format_movie(cls, movie_object):
        """returns formatted `Movie` object

        """
        return {'id': movie_object.id,
                'movie_name': movie_object.name
                }

    @classmethod
    def get_all_movies(cls):
        """This method return a formatted dict of all the Movie objects

        """
        return list(map(cls.format_movie, db_session.query(Movie).all()))
