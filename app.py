from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_basicauth import BasicAuth

from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.database_uri
db = SQLAlchemy(app)
mm = Marshmallow(app)
basic_auth = BasicAuth(app)
