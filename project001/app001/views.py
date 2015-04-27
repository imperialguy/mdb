from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from app001.models import Movie


class MovieCreate(CreateView):
    model = Movie
    fields = ['name']


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name']
    template_name_suffix = '_update_form'


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('list-movies')


def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})
