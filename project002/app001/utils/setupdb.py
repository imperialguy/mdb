from app001.utils.settings import Base, DB_ENGINE
from app001.utils.mappings import Movie

TABLE_MAPPINGS = [Base.metadata.tables[Movie.__tablename__],
                  ]


def refresh():
    drop_all_tables()
    create_all_tables()


def create_all_tables():
    Base.metadata.create_all(DB_ENGINE, TABLE_MAPPINGS)


def drop_all_tables():
    Base.metadata.drop_all(DB_ENGINE, TABLE_MAPPINGS)
