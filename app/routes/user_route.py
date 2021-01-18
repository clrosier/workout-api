from app import api, authorizations
from app.models.db_models.user_model import User
from app.models.api_models.user_model import register_model, login_model

from app.controllers.user_controller import register_user, login_user, logout_user

from flask import jsonify, request
from flask_restx import Resource, fields

from passlib.context import CryptContext


ns_user = api.namespace('users', description='User management API')

@ns_user.route('/')
class Users(Resource):
    """
    GET to this resource returns all users
    """
    def get(self):
        result = User.query.all()
        users = [user.to_dict() for user in result]
        return jsonify(users)


@ns_user.route('/register')
class Register(Resource):
    @api.expect(register_model)
    def post(self):
        data = api.payload

        response = register_user(data)
        if response['status'] != 201:
            return response['message'], response['status']
        else:
            return response['auth_token'], response['status']


@ns_user.route('/login')
class Login(Resource):
    """
    GET to this resource returns number of logged in users
    POST to this resource attempts a login
    """
    def get(self):
        pass


    @api.expect(login_model)
    def post(self):
        data = api.payload
        
        response = login_user(data)
        if response['status'] != 200:
            return response['message'], response['status']
        else:
            return response['payload'], response['status']


@ns_user.route('/logout')
class Logout(Resource):
    """
    POST to this resource attempts a logout
    """
    
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Authorization token.'}})
    def post(self):

        response = logout_user(request)
        return response['message'], response['status']

