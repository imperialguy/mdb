from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime
from app001.utils.settings import Base, TABLE_ARGS


class Movie(Base):
    __tablename__ = 'movie'
    __table_args__ = TABLE_ARGS

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_changed_at = Column(
        DateTime, default=datetime.today().date(),
        onupdate=datetime.today().date())
