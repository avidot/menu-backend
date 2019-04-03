from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ingredient(Base):
	__tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name =  Column(String(100))