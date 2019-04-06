# -*- coding: UTF-8 -*-

from database.DatabaseEngine import db
from model.IngredientCategoryEnum import IngredientCategoryEnum

class Ingredient(db.Model):
	__tablename__ = 'ingredients'
	name =  db.Column(db.String(100), primary_key=True)
	category =  db.Column(db.Enum(IngredientCategoryEnum))