from app import db
from flask_sqlalchemy import inspect


class Categories(db.Model):
    __tablename__ = "categories"
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True)
    category_description = db.Column(db.String(255))


    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    
    def __repr__(self):
        return '<Category %r>' % self.category_name


    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }