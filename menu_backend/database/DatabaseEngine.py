""" SQL Alchemy Engine for MySQL """
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from menu_backend.utils.commons import app

db = SQLAlchemy(app, session_options={"autoflush": False})