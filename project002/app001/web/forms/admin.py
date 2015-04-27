from wtforms import (
    Form,
    validators,
    TextField,
    ValidationError
)
from app001.web.models.admin import Admin


class NewMovieForm(Form):

    """ Form for new movie

    """
    name = TextField(u'name', [validators.required()])

    def validate_name(form, field):
        """Validates the existence of the movie name in the database

        """
        if Admin(movie_name=field.data).movie_exists():
            raise ValidationError("This movie already exists in our system")
