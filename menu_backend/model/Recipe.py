from database.MysqlEngine import db


recipes_ingredients = db.Table('recipes_ingredients',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True),
	db.Column('amount', db.Integer),
	db.Column('unit', db.String(50))
)

class Recipe(db.Model):
	__tablename__ = 'recipes'
	id = db.Column(db.Integer, primary_key=True)
	name =  db.Column(db.String(100))
	ingredients = db.relationship('Ingredient', secondary=recipes_ingredients, lazy='subquery',
        backref=db.backref('recipes', lazy=True))
