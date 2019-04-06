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