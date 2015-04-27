from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Statements for enabling the development environment
DEBUG = True
USE_RELOADER = False

# Define the database parameters
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
DB_ENGINE = create_engine(SQLALCHEMY_DATABASE_URI)
DB_SESSION_AUTOFLUSH = True
DB_SESSION_AUTOCOMMIT = False
DB_SESSION_EXPIRE_ON_COMMIT = True

# Create and configure a SQL Alchemy session object
DB_SESSION_MAKER = sessionmaker()
DB_SESSION_MAKER.configure(bind=DB_ENGINE,
                           autoflush=DB_SESSION_AUTOFLUSH,
                           autocommit=DB_SESSION_AUTOCOMMIT,
                           expire_on_commit=DB_SESSION_EXPIRE_ON_COMMIT)

# This is our Flask persistent DB session
DB_SESSION = DB_SESSION_MAKER()

# Declarative Base for sql alchemy mappings
Base = declarative_base()

# Table arguments for sql alchemy mappings
TABLE_ARGS = {'useexisting': True}
