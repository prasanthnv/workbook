import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# Controllers
# from workbook.controllers.user import UserController

db = SQLAlchemy()
app = Flask(__name__)
api = Api(app)

basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
ma = Marshmallow(app)
db.init_app(app)

with app.app_context():
    db.create_all()
