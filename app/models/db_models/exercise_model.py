from app import db
from flask_sqlalchemy import inspect

class Exercises(db.Model):
    __tablename__ = "exercises"
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(30), unique=True)
    exercise_description = db.Column(db.String(255))

    
    def __init__(self, exercise_name, exercise_description):
        self.exercise_name = exercise_name
        self.exercise_description = exercise_description


    def __repr__(self):
        return '<Exercise %r>' % self.exercise_name
    

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


class ExerciseCategories(db.Model):
    __tablename__ = "exercise_categories"
    ex_cat_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ex_name = db.Column(db.String(30), db.ForeignKey('exercises.exercise_name'))
    cat_name = db.Column(db.String(30), db.ForeignKey('categories.category_name'))


    def __init__(self, ex_name, cat_name):
        self.ex_name = ex_name
        self.cat_name = cat_name
    

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

