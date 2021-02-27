from app import db
from app.models.db_models.program_model import Program

from app.util.token import encode_auth_token, decode_auth_token


def add_program(data, request):
    print(data)
    response = {
        "status": 400,
        "message": "Program adding failed."
    }
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header
    else:
        auth_token = ''
    
    if auth_token:
        resp = decode_auth_token(auth_token)
        if isinstance(resp, int):
            user_id = resp
            new_program = Program(
                program_name=data['program_name'],
                program_data=data['program_data'],
                program_owner=user_id
            )
            try:
                db.session.add(new_program)
                db.session.commit()

                response = {
                    "status": 201,
                    "message": "New program creation successful.",
                }
            except Exception as e:
                response = {
                    "state": 500,
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



