from app import api
from app.models.db_models.exercise_model import Exercises, ExerciseCategories
from app.models.api_models.exercise_model import exercise_model
from app.controllers.exercise_controller import add_exercise
from app.util.exercise_util import exercises_with_categories

from flask import jsonify
from flask_restx import Resource, fields


ns_exercise = api.namespace('exercises', description='Management of exercises')

@ns_exercise.route('/')
class Exercise(Resource):
    """
    GET to this resource returns all exercises
    POST to this resource inserts a new exercise
    """
    def get(self):
        result = Exercises.query.all()
        exercises = [exercise.to_dict()['exercise_name'] for exercise in result]
        print(exercises)
        return jsonify(exercises)
    
    @api.expect(exercise_model)
    def post(self):
        data = api.payload

        response = add_exercise(data)
        return response['message'], response['status']


@ns_exercise.route('/<string:ex_name>')
class SingleExercise(Resource):
    """
    GET to this resource gets a single exercise
    """
    def get(self, ex_name):
        result = Exercises.query.filter_by(exercise_name=ex_name).first().to_dict()
        exercise = {
            "exercise_name": result['exercise_name'],
            "exercise_desc": result['exercise_description']
        }
        return jsonify(exercise)


@ns_exercise.route('/exercise_categories')
class ExercisesWithCategories(Resource):
    """
    GET to this resource to get exercises with their categories
    """
    def get(self):
        result = ExerciseCategories.query.all()
        exercise_categories = [ex_cat.to_dict() for ex_cat in result]
        return jsonify(exercises_with_categories(exercise_categories))

