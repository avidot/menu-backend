""" Command InstallDb : Use for install the database structure """
# -*- coding: utf-8 -*-

import click
from menu_backend.database.DatabaseEngine import db
from menu_backend.model.Menu import Menu
from menu_backend.model.Recipe import Recipe
from menu_backend.model.Ingredient import Ingredient
from menu_backend.model.RecipeIngredient import RecipeIngredient


@click.group()
def manageDb():
	pass

@manageDb.command()
def installDb():
	db.create_all()

@manageDb.command()
def dropDb():
	db.drop_all()