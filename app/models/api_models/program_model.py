from app import api
from flask_restx import fields

program_model = api.model('Add Program', {
    'program_name': fields.String(required=True, description='The name of the program.'),
    'program_data': fields.String(required=True, description='The data of the program (the strigified json)')
})