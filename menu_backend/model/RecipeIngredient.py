from database.DatabaseEngine import db

class RecipeIngredient(db.Model):
	__tablename__ = 'recipes_ingredients'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
	amount =  db.Column(db.Integer)
	unit =  db.Column(db.String(50))
	
	recipe = db.relationship("Recipe", backref="recipe_link")
	ingredient = db.relationship("Ingredient", backref="ingredient_link")
