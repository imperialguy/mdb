from setuptools import setup, find_packages

requires = [
    'coverage==4.0a5',
    'Django==1.8',
    'Flask==0.10.1',
    'itsdangerous==0.24',
    'Jinja2==2.7.3',
    'MarkupSafe==0.23',
    'nose==1.3.4',
    'pep8==1.6.2',
    'SQLAlchemy==0.9.9',
    'Werkzeug==0.10.1',
    'unittest2==1.0.1',
    'WTForms==2.0.2',
    'django-environ>=0.3.0',
    'django-braces>=1.4.0',
    'django-crispy-forms>=1.4.0',
    'django-admin-bootstrapped>=1.6.9',
    'django-debug-toolbar>=1.2.1',
    'pudb==2014.1'
]

tests_require = requires

docs_extras = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface']

setup(name='mdb',
      version='0.1',
      description='mdb',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Django/Flask",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application", ],
      author='',
      author_email='vpkcareer2011@gmail.com',
      url='',
      keywords='web wsgi django flask',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          'docs': docs_extras, },
      entry_points="""\
      """,
      )
