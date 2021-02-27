from app import api
from flask_restx import fields

exercise_model = api.model('Add Exercise', {
    'exercise_name': fields.String(required=True, description='The name of the exercise.'),
    'exercise_description': fields.String(required=True, descripttion='The description of the new exercise.'),
    'exercise_categories': fields.List(fields.String(), required=True)
})