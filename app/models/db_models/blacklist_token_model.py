from app import db
from flask_sqlalchemy import inspect

from datetime import datetime

class BlacklistToken(db.Model):
    __tablename__ = "blacklist_tokens"
    token_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)


    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.now()
    

    def __repr__(self):
        return '<id: token: {}>'.format(self.token)