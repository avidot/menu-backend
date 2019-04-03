""" Command InstallDb : Use for install the database structure """
# -*- coding: utf-8 -*-

import click
from database.MysqlEngine import db
from model.Recipe import Recipe
from model.Ingredient import Ingredient

@click.command()
def cli():
	db.create_all()
	click.echo("test")
