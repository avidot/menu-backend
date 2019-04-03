""" Init the appmication """
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask("menu_backend")
sqlUrl = "mysql+mysqldb://user_menu:pwd_menu@"
sqlUrl = sqlUrl +"localhost:3306"+"/menu_backend"
app.config['SQLALCHEMY_DATABASE_URI'] = sqlUrl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False