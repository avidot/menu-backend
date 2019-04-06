""" Command InstallDb : Use for install the database structure """
# -*- coding: utf-8 -*-

import click
from database.DatabaseEngine import db
from model.Menu import Menu
from model.Recipe import Recipe
from model.Ingredient import Ingredient
from model.RecipeIngredient import RecipeIngredient


@click.group()
def manageDb():
	pass

@manageDb.command()
def installDb():
	db.create_all()

@manageDb.command()
def dropDb():
	db.drop_all()