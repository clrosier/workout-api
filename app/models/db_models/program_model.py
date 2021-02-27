from app import db
from flask_sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import JSON

from app.models.db_models.user_model import User


class Program(db.Model):
    __tablename__ = "programs"
    program_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    program_name = db.Column(db.String(64), unique=True, nullable=False)
    program_data = db.Column(JSON)
    program_owner = db.Column(db.String(32), nullable=False)
