import os
import yaml

from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r'/*': {'origins': '*'}})

cfg_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.yaml')

with open(cfg_file) as cfg:
    app_config = yaml.safe_load(cfg)

# Initialize database connection with SQLAlchemy
db_uri = "postgres://{}:{}@{}:{}/{}".format(
    app_config['app']['db']['user'],
    app_config['app']['db']['pass'],
    app_config['app']['db']['host'],
    app_config['app']['db']['port'],
    app_config['app']['db']['name']
)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.routes.exercise_route import *
from app.routes.category_route import *


# Start the service
if __name__ == '__main__':
    app.run(debug=True)