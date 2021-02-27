from app import api, authorizations
from app.models.db_models.program_model import Program
from app.models.api_models.program_model import program_model

from app.controllers.program_controller import add_program

from flask import jsonify, request
from flask_restx import Resource, fields


ns_program = api.namespace('programs', description="Program management API")


@ns_program.route('/')
class Programs(Resource):
    """
    GET to this resource returns all programs
    """
    def get(self):
        pass


@ns_program.route('/add')
class AddProgram(Resource):
    """
    POST to this resource adds a new program
    """
    @api.expect(program_model)
    def post(self):
        data = api.payload

        response = add_program(data, request)
        return response['message'], response['status']
