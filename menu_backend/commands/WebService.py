""" Command WebService : Use for manage recipes operations """
# -*- coding: utf-8 -*-

import click
import json
from flask import request, Response
from utils.commons import app
from model.Menu import Menu
from model.Recipe import Recipe
from database.RecipeController import addRecipe, deleteRecipe, updateRecipe
from database.MenuController import addMenu, deleteMenu, updateMenu


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

@app.route('/recipes/<recipeName>', methods=['PUT', 'DELETE'])
def manageRecipe(recipeName):
	if request.method == 'PUT':
		updateRecipe(recipeName, request.json)
		resp = Response(status=204)
		return resp
	else:
		deleteRecipe(recipeName)
		resp = Response(status=204)
		return resp

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

@app.route('/menus/<menuDay>-<menuMeal>', methods=['PUT', 'DELETE'])
def manageMenu(menuDay, menuMeal):
	if request.method == 'PUT':
		updateMenu(menuDay, menuMeal, request.json)
		resp = Response(status=204)
		return resp
	else:
		deleteMenu(menuDay, menuMeal)
		resp = Response(status=204)
		return resp

@click.command()
def startWebService():
	click.echo("Start WebService")
	app.run(debug=True)