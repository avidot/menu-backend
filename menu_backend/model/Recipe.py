# -*- coding: UTF-8 -*-

from menu_backend.database.DatabaseEngine import db

class Recipe(db.Model):
	__tablename__ = 'recipes'
	name =  db.Column(db.String(100), primary_key=True)
	ingredients = db.relationship('Ingredient', secondary="recipes_ingredients",
        backref=db.backref('recipes', lazy=True))

	recipe_link = []

	def getRecipeDict(self):
		recipe = {}
		recipe["name"] = self.name
		recipe["ingredients"] = []
		for recipeIngredient in self.recipe_link:
			for ingredient in self.ingredients:
				if ingredient.name == recipeIngredient.ingredient_name:
					ingedientJson = {}
					ingedientJson["name"] = ingredient.name
					ingedientJson["category"] = ingredient.category.value
					ingedientJson["amount"] = recipeIngredient.amount
					ingedientJson["unit"] = recipeIngredient.unit.value
					recipe["ingredients"].append(ingedientJson)
		return recipe