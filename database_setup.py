from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Items(Base):
    __tablename__ = 'items'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
          'id': self.id,
           'name': self.name,
           'description' : self.description
       }



engine = create_engine('sqlite:///items.db')
Base.metadata.create_all(engine)
