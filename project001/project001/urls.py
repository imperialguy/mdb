from app001.views import MovieCreate, MovieUpdate, MovieDelete, list_movies
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'movie/add/$', MovieCreate.as_view(), name='movie-add'),
    url(r'movie/(?P<pk>[0-9]+)/$', MovieUpdate.as_view(), name='movie-update'),
    url(r'movie/(?P<pk>[0-9]+)/delete/$',
        MovieDelete.as_view(), name='movie-delete'),
    url(r'^movies/', list_movies, name='list-movies'),
    url(r'^admin/', include(admin.site.urls)),
]
