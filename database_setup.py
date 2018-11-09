import sys

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
  __tablename__ = "Category"

  name =Column(String(80), nullable = False)
  id = Column(Integer, primary_key = True)



class Item(Base):
    __tablename__ = 'item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer, ForeignKey('category_id.id'))
    category = relationship(Category)


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
