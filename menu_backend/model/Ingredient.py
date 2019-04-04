# -*- coding: UTF-8 -*-

from database.DatabaseEngine import db

class Ingredient(db.Model):
	__tablename__ = 'ingredients'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name =  db.Column(db.String(100))