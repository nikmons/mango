#!mongo_api/app.py
import os
import datetime

from flask import Flask, jsonify, abort, make_response, render_template
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__, static_url_path="")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["ENVIRONMENT"] = os.getenv("ENV")
app.config["CSRF_ENABLED"] = True
app.config["SWAGGER"] = {"title":"Swagger JWT Authentication App", "uiversion":3}
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)
db = SQLAlchemy(app)

from models import models

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")