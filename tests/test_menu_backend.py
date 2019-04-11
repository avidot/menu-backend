#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `menu_backend` package."""

import unittest
from click.testing import CliRunner
from menu_backend import cli
from menu_backend.model.Recipe import Recipe
from menu_backend.model.RecipeIngredient import RecipeIngredient
from menu_backend.model.Ingredient import Ingredient
from menu_backend.model.IngredientCategoryEnum import IngredientCategoryEnum
from menu_backend.model.UnitEnum import UnitEnum


class test_menu_backend(unittest.TestCase):
    """Tests for `menu_backend` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        cli.main()
        runner = CliRunner()
        result = runner.invoke(cli.cli)
        assert result.exit_code == 0
        assert "managedb" in result.output
        assert "startwebservice" in result.output
        assert '--help  Show this message and exit.' in result.output

    def test_get_recipe_dict(self):
        """Test get recipe dict."""
        recipe = Recipe(name="Recipe1")
        recipeIngredient = RecipeIngredient(recipe_name="Recipe1", ingredient_name="ing1", amount=10, unit=UnitEnum("g"))
        recipe.recipe_link.append(recipeIngredient)
        recipe.ingredients.append(Ingredient(name="ing1", category=IngredientCategoryEnum("Alimentary")))
        assert recipe.getRecipeDict()["name"] == "Recipe1"
        assert len(recipe.getRecipeDict()["ingredients"]) == 1
