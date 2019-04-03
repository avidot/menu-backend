""" SQL Alchemy Engine for MySQL """
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

class MysqlEngineMetaCLass(type):
	""" A metaclass that creates a Singleton base class when called. """
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MysqlEngineMetaCLass, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class MysqlEngine(metaclass=MysqlEngineMetaCLass):

	def setFlaskApp(self, app):
		""" Set the flask app """
		self.db = SQLAlchemy(app)
