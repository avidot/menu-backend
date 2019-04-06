""" Command WebService : Use for manage recipes operations """
# -*- coding: utf-8 -*-

import click
import json
from flask import request, Response
from utils.commons import app
from database.DatabaseEngine import db
from model.Menu import Menu
from model.Recipe import Recipe
from database.RecipeController import addRecipe
from database.MenuController import addMenu


@app.route('/recipes', methods=['GET', 'POST'])
def manageAllRecipes():
	if request.method == 'GET':
		allRecipes = Recipe.query.order_by(Recipe.name).all()
		allRecipesDict = [r.getRecipeDict() for r in allRecipes]
		js = json.dumps(allRecipesDict)
		resp = Response(js, status=200, mimetype='application/json')
		return resp
	else:
		addRecipe(request.json)
		resp = Response(status=201)
		return resp

@app.route('/recipes/<recipeId>', methods=['PUT', 'DELETE'])
def manageRecipe(recipeId):
	recipeToManage = Recipe.query.filter_by(id=recipeId).first()
	if recipeToManage:
		if request.method == 'PUT':
			print("Update recipe")
			return json.dumps(Recipe.query.order_by(Recipe.name).all())
		else:
			db.session.delete(recipeToManage)
			db.session.commit()
			return "Create recipe"

@app.route('/menus', methods=['GET', 'POST'])
def manageAllMenus():
	if request.method == 'GET':
		allMenus = Menu.query.all()
		allMenusDict = [r.getMenuDict() for r in allMenus]
		js = json.dumps(allMenusDict)
		resp = Response(js, status=200, mimetype='application/json')
		return resp
	else:
		addMenu(request.json)
		resp = Response(status=201)
		return resp

@click.command()
def startWebService():
	click.echo("Start WebService")
	app.run(debug=True)