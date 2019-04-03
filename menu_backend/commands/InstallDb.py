""" Command InstallDb : Use for install the database structure """
# -*- coding: utf-8 -*-

import click
from utils.GetFlaskApp import getFlaskApp
from database.MysqlEngine import MysqlEngine

@click.command()
def cli():
	app = getFlaskApp()

	test = MysqlEngine()
	test.setFlaskApp(app)
	test.db.create_all()
