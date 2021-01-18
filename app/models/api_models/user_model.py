from app import api
from flask_restx import fields

register_model = api.model('Register', {
    'username': fields.String(required=True, description='Username for logging in.'),
    'password': fields.String(required=True, description='Password for logging in.'),
    'first_name': fields.String(required=True, description='First Name'),
    'last_name': fields.String(required=True, description='Last Name'),
    'email': fields.String(required=True, description='Email address of user'),
})

login_model = api.model('Login', {
    'email': fields.String(required=True, description='Email for logging in'),
    'password': fields.String(required=True, description='Password for logging in')
})
