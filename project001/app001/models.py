from django.core.urlresolvers import reverse
from django.db import models


class Movie(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Movie Name', unique=True)

    def get_absolute_url(self):
        return reverse('list-movies')
