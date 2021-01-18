import jwt
from datetime import datetime, timedelta

from app import app_config

def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=43200),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app_config['app']['auth']['SECRET_KEY'],
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    print(auth_token)
    try:
        payload = jwt.decode(auth_token, app_config['app']['auth']['SECRET_KEY'], algorithms="HS256")
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'