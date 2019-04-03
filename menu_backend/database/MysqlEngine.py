""" SQL Alchemy Engine for MySQL """
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from utils.commons import app

db = SQLAlchemy(app)