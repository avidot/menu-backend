# -*- coding: UTF-8 -*-

from menu_backend.database.DatabaseEngine import db
from menu_backend.model.DayEnum import DayEnum
from menu_backend.model.MealEnum import MealEnum

class Menu(db.Model):
	__tablename__ = 'menus'
	day =  db.Column(db.Enum(DayEnum), primary_key=True)
	meal =  db.Column(db.Enum(MealEnum), primary_key=True)
	recipe_name = db.Column(db.String(100), db.ForeignKey('recipes.name'))

	recipe = db.relationship("Recipe", backref="recipes")

	def getMenuDict(self):
		menu = {}
		menu["day"] = self.day.value
		menu["meal"] = self.meal.value
		menu["recipeName"] = self.recipe_name
		return menu