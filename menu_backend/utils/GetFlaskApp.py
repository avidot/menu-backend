""" GetFlaskApp : Return the flask app """
# -*- coding: utf-8 -*-

from flask import Flask


def getFlaskApp():
	app = Flask("menu_backend")
	sqlUrl = "mysql+mysqldb://testmenu1:menuBackUser!1&@"
	sqlUrl = sqlUrl +"100.121.67.120:3306"+"/menu_backend"
	app.config['SQLALCHEMY_DATABASE_URI'] = sqlUrl
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	return app
