""" Igredient Controller : Manage storage function for Ingredient """
# -*- coding: utf-8 -*-

from database.DatabaseEngine import db
from model.Ingredient import Ingredient

def getIngredient(ingredientName):
	return Ingredient.query.filter_by(name=ingredientName).first()

def addIngredient(ingredientJson):
	if not getIngredient(ingredientJson["name"]):
		ingredient = Ingredient(name=ingredientJson["name"])
		db.session.commit()
		return ingredient
	return None