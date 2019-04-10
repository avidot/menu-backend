# -*- coding: UTF-8 -*-

from menu_backend.database.DatabaseEngine import db
from menu_backend.model.IngredientCategoryEnum import IngredientCategoryEnum

class Ingredient(db.Model):
	__tablename__ = 'ingredients'
	name =  db.Column(db.String(100), primary_key=True)
	category =  db.Column(db.Enum(IngredientCategoryEnum))