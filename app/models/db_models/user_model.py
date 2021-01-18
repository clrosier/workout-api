from app import db
from flask_sqlalchemy import inspect


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    admin_user = db.Column(db.Boolean, nullable=False, default=False)
    logged_in = db.Column(db.Boolean, nullable=False, default=False)
    profile_image = db.Column(db.String(200))

    
    def __init__(self, username, password_hash, first_name, last_name, email, admin_user, logged_in, profile_image):
        self.username = username
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.admin_user = admin_user
        self.logged_in = logged_in
        self.profile_image = profile_image
    

    def __repr__(self):
        return '<User %r>' % self.username
    

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

