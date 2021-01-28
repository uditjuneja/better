# from flask_restless import APIManager

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)

app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
api = Api(app)

from .models import *
from .resource import *

api.add_resource(Parking, "/parking")
api.add_resource(Floors, "/floor")
