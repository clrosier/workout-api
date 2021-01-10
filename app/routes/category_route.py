from app import api, db
from app.models.db_models.category_model import Categories

from flask import jsonify
from flask_restx import Resource, fields


ns_category = api.namespace('Exercise Operations', description='Management of exercise categories')

@api.route('/categories')
class Category(Resource):
    """
    GET to this resource returns all categories
    POST to this resource inserts a new category
    """
    def get(self):
        result = Categories.query.all()
        categories = [category.to_dict()['category_name'] for category in result]
        return jsonify(categories)
    

    def post(self):
        pass


@api.route('/categories/<string:cat_name>')
class SingleCategory(Resource):
    """
    GET to this resource gets a single exercise
    """
    def get(self, cat_name):
        result = Categories.query.filter_by(category_name=cat_name).first().to_dict()
        category = {
            "category_name": result['category_name'],
            "category_desc": result['category_description']
        }
        return jsonify(category)
