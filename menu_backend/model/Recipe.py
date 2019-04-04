# -*- coding: UTF-8 -*-

import json
from database.DatabaseEngine import db

class Recipe(db.Model):
	__tablename__ = 'recipes'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name =  db.Column(db.String(100))
	ingredients = db.relationship('Ingredient', secondary="recipes_ingredients", lazy='subquery',
        backref=db.backref('recipes', lazy=True))

	def getRecipeDict(self):
		recipe = {}
		recipe["name"] = self.name
		recipe["ingredients"] = []
		for ingredient in self.ingredients:
			ingedientJson = {}
			ingedientJson["name"] = ingredient.name
			recipe["ingredients"].append(ingedientJson)
		return recipe