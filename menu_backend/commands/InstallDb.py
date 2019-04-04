""" Command InstallDb : Use for install the database structure """
# -*- coding: utf-8 -*-

import click
import logging
from database.DatabaseEngine import db
from model.Recipe import Recipe
from model.Ingredient import Ingredient
from model.RecipeIngredient import RecipeIngredient

@click.command()
def installDb():
	logging.info("Start create database structure")
	db.create_all()
