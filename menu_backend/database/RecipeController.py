""" Recipe Controller : Manage storage function for Recipe """
# -*- coding: utf-8 -*-

from database.DatabaseEngine import db
from model.Recipe import Recipe
from model.RecipeIngredient import RecipeIngredient
from model.UnitEnum import UnitEnum
from database.IngredientController import addIngredient, getIngredient

def addRecipe(recipeJson):
	recipe = Recipe(name=recipeJson["name"])
	db.session.add(recipe)
	for ingredient in recipeJson["ingredients"]:
		newIngredient = getIngredient(ingredient["name"])
		if not newIngredient:
			newIngredient = addIngredient(ingredient)
		recipeIngredientLink = RecipeIngredient(recipe_name=recipe.name,ingredient_name=newIngredient.name, 
			amount=ingredient["amount"], unit=UnitEnum(ingredient["unit"]))
		db.session.add(recipeIngredientLink)
	db.session.commit()

def updateRecipe(recipeName, recipeJson):
	recipeToManage = Recipe.query.filter_by(name=recipeName).first()
	allIngredientNames = [ingredient["name"] for ingredient in recipeJson["ingredients"]]
	ingredientsToUnlink = [ingredient for ingredient in recipeToManage.ingredients if ingredient.name not in allIngredientNames]
	for ingredient in ingredientsToUnlink:
		recipeToManage.ingredients.remove(ingredient)
	for ingredient in recipeJson["ingredients"]:
		newIngredient = getIngredient(ingredient["name"])
		if not newIngredient:
			newIngredient = addIngredient(ingredient)
		recipeIngredientLink = RecipeIngredient.query.filter_by(recipe_name=recipeToManage.name,ingredient_name=newIngredient.name).first()
		if not recipeIngredientLink:
			recipeIngredientLink = RecipeIngredient(recipe_name=recipeToManage.name,ingredient_name=newIngredient.name, 
				amount=ingredient["amount"], unit=UnitEnum(ingredient["unit"]))
			db.session.add(recipeIngredientLink)
		else :
			recipeIngredientLink.amount = ingredient["amount"]
			recipeIngredientLink.unit = UnitEnum(ingredient["unit"])
	db.session.commit()

def deleteRecipe(recipeName):
	recipeToManage = Recipe.query.filter_by(name=recipeName).first()
	print(recipeName)
	if recipeToManage:
		db.session.delete(recipeToManage)
		db.session.commit()