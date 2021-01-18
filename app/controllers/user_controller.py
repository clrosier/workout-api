from app import db
from app.models.db_models.user_model import User
from app.models.db_models.blacklist_token_model import BlacklistToken

from app.util.token import encode_auth_token, decode_auth_token

from passlib.context import CryptContext

def register_user(data):

    response = {
        "status": 409,
        "message": "The username or email is already in use."
    }
    pwd_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
    )

    # If username and email does not already exist
    if User.query.filter_by(username=data['username']).first() == None and User.query.filter_by(email=data['email']).first() == None:
        new_user = User(
            username=data['username'],
            password_hash=pwd_context.encrypt(data['password']),
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            admin_user=False,
            logged_in=False,
            profile_image=None

        )
        db.session.add(new_user)
        db.session.commit()

        auth_token = encode_auth_token(new_user.user_id)
        response = {
            "status": 201,
            "message": "Registration successful.",
            "auth_token": auth_token
        }
    
    return response


def login_user(data):

    response = {
        "status": 404,
        "message": "The username does not exist."
    }

    pwd_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
    )

    # Check if username exists
    login_user = User.query.filter_by(email=data['email']).first()
    if login_user != None:
        
        # Check password versus hashed password
        if pwd_context.verify(data['password'], login_user.password_hash):
            
            auth_token = encode_auth_token(login_user.user_id)
            response = {
                "status": 200,
                "message": "Login successful.",
                "payload": {
                    "auth_token": auth_token,
                    "username": login_user.username,
                    "firstname": login_user.first_name,
                    "lastname": login_user.last_name,
                    "email": login_user.email,
                    "admin_user": login_user.admin_user,
                    "profile_image": login_user.profile_image
                }
            }
        else:
            response = {
                "status": 401,
                "message": "Invalid email or password.",
            }
    
    return response


def logout_user(request):
    response = {
        "status": 400,
        "message": "Logout failed."
    }

    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header
    else:
        auth_token = ''
    
    if auth_token:
        resp = decode_auth_token(auth_token)
        if isinstance(resp, str):
            blacklist_token = BlacklistToken(token=auth_token)
            try:
                db.session.add(blacklist_token)
                db.session.commit()
                response = {
                    "status": 200,
                    "message": 'Logout successful.'
                }
            except Exception as e:
                response = {
                    "status": 500,
                    "message": str(e)
                }
        else:
            response = {
                "status": 401,
                "message": str(resp)
            }
    else:
        response = {
            "status": 403,
            "message": "Provide a valid authorization token."
        }
    
    return response
