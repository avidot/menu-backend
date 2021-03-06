from menu_backend.database.DatabaseEngine import db
from menu_backend.model.UnitEnum import UnitEnum

class RecipeIngredient(db.Model):
	__tablename__ = 'recipes_ingredients'
	recipe_name = db.Column(db.String(100), db.ForeignKey('recipes.name'), primary_key=True)
	ingredient_name = db.Column(db.String(100), db.ForeignKey('ingredients.name'), primary_key=True)
	amount =  db.Column(db.Integer)
	unit =  db.Column(db.Enum(UnitEnum))
