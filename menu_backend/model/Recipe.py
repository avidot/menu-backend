from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table('recipes_ingredients', Base.metadata,
    Column('id_recipe', Integer, ForeignKey('recipes.id')),
    Column('id_ingredient', Integer, ForeignKey('ingredients.id')),
    Column('amount', Integer),
    Column('unit', String(50))
)

class Recipe(Base):
	__tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name =  Column(String(100))
    ingredients = relationship("Ingredient", secondary=association_table)
