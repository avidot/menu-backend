""" Menu Controller : Manage storage function for Menu """
# -*- coding: utf-8 -*-

from database.DatabaseEngine import db
from model.Menu import Menu
from model.DayEnum import DayEnum
from model.MealEnum import MealEnum

def addMenu(menuJson):
	menu = Menu(day=DayEnum(menuJson["day"]),meal=MealEnum(menuJson["meal"]),
		recipe_name=menuJson["recipeName"])
	db.session.add(menu)
	db.session.commit()

def updateMenu(menuDay, menuMeal, menuJson):
	menuToManage = Menu.query.filter_by(day=DayEnum(menuDay), meal=MealEnum(menuMeal)).first()
	menuToManage.recipe_name = menuJson["recipeName"]
	db.session.commit()

def deleteMenu(menuDay, menuMeal):
	menuToManage = Menu.query.filter_by(day=DayEnum(menuDay), meal=MealEnum(menuMeal)).first()
	db.session.delete(menuToManage)
	db.session.commit()