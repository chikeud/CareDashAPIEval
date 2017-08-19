__author__ = 'ChikeUdenze'


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from setting import DB_URI

Session = sessionmaker(autocommit=False, autoflush=False,bind=create_engine(DB_URI))
session = scoped_session(Session)