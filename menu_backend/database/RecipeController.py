""" Recipe Controller : Manage storage function for Recipe """
# -*- coding: utf-8 -*-

from database.DatabaseEngine import db
from model.Recipe import Recipe
from model.RecipeIngredient import RecipeIngredient
from model.UnitEnum import UnitEnum
from database.IngredientController import addIngredient, getIngredient

def addRecipe(recipeJson):
	recipe = Recipe(name=recipeJson["name"])
	for ingredient in recipeJson["ingredients"]:
		newIngredient = getIngredient(ingredient["name"])
		if not newIngredient:
			newIngredient = addIngredient(ingredient)
		recipeIngredientLink = RecipeIngredient(recipe=recipe,ingredient=newIngredient, amount=ingredient["amount"], 
			unit=UnitEnum(ingredient["unit"]))
		db.session.add(recipeIngredientLink)
	db.session.add(recipe)
	db.session.commit()