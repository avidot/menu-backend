""" Igredient Controller : Manage storage function for Ingredient """
# -*- coding: utf-8 -*-

from menu_backend.database.DatabaseEngine import db
from menu_backend.model.Ingredient import Ingredient
from menu_backend.model.IngredientCategoryEnum import IngredientCategoryEnum

def getIngredient(ingredientName):
	return Ingredient.query.filter_by(name=ingredientName).first()

def addIngredient(ingredientJson):
	if not getIngredient(ingredientJson["name"]):
		ingredient = Ingredient(name=ingredientJson["name"], category=IngredientCategoryEnum(ingredientJson["category"]))
		db.session.add(ingredient)
		db.session.commit()
		return ingredient
	return None