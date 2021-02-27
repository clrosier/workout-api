from app import db
from app.models.db_models.exercise_model import Exercises, ExerciseCategories


def add_exercise(data):
    response = {
        "status": 409,
        "message": "This exercise already exists in the database"
    }

    if Exercises.query.filter_by(exercise_name=data['exercise_name']).first() == None:
        new_exercise = Exercises(
            exercise_name=data['exercise_name'],
            exercise_description=data['exercise_description']
        )
        db.session.add(new_exercise)
        
        for category in data['exercise_categories']:
            print(category)
            new_exercise_category = ExerciseCategories(
                ex_name=data['exercise_name'],
                cat_name=category
            )
            db.session.add(new_exercise_category)

        db.session.commit()
        response = {
            "status": 201,
            "message": "New exercise successfully added.",
        }
    return response
