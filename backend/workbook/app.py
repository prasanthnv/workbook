import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


# Controllers
# from workbook.controllers.user import UserController
db = SQLAlchemy()
app = Flask(__name__)

# swagger
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "WorkBook"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
api = Api(app, prefix='/api/v1')

basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
ma = Marshmallow(app)
migrate = Migrate(app, db)


db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    db.create_all()
