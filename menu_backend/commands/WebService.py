""" Command WebService : Use for install the database structure """
# -*- coding: utf-8 -*-

import click
from database.MysqlEngine import MysqlEngine
from utils.GetFlaskApp import getFlaskApp

@click.command()
def cli():
	app = getFlaskApp()

	test = MysqlEngine()
	test.setFlaskApp(app)

	click.echo(test.db)
