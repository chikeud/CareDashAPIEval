__author__ = 'ChikeUdenze'
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    reviews = Column(ARRAY)

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    description = Column(String)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from setting import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)