# mdb
simple movie database

Initial Steps:
1. Create a virtual env on your machine with Python 3.x
2. switch to your virtual env
3. cd <path_to_mdb_repo>
4. python setup.py develop


project001: django-based

If you want to check out the django-based project:

1. cd <path_to_mdb_repo>/project001/
2. python manage.py migrate
3. python manage.py runserver
4. Open a browser and go to:
	4.1 localhost:8000/movie/add --> to add a movie
	4.2 localhost:8000/movie/<movie_id> --> to update a movie name
	4.3 localhost:8000/movie/<movie_id>/delete --> to delete a movie from the db
	4.4 localhost:8000/movies --> to list all movies

project002: flask/sqla based

I also added a sample flask/sqla based project. To do a test run on that:

1. cd <path_to_mdb_repo>/project002
2. python app001/testrun.py

If all goes well, it should appear something like this:

(your_virtual_env)$ python app001/testrun.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.042s

OK