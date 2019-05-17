#!mongo_api/app.py
import os
import datetime

from flask import (
    Flask, jsonify, abort, make_response, render_template
)
from flask_restful import (
    Api, Resource, reqparse, fields, marshal
)
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, create_refresh_token,
    jwt_refresh_token_required, get_raw_jwt
)
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from

from dotenv import load_dotenv
load_dotenv(verbose=True)

app = Flask(__name__, static_url_path="")
app.secret_key = os.getenv("FLASK_SECRET_KEY") # Load from env var
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["ENVIRONMENT"] = os.getenv("ENV")
app.config["CSRF_ENABLED"] = True
app.config["SWAGGER"] = {"title":"Swagger JWT Authentication App", "uiversion":3}
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

swagger_template={
        "openapi": "2.0.0",
        "info": {
            "title": "Mango (JWT Auth)",
            "version": "1.0",
        },
        "securityDefinitions": {
            "Bearer":{
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        },
        "produces": [
            "application/json",
        ],
        "security": [
            {"Bearer": "[]"}
        ]
    }

api = Api(app)
db = SQLAlchemy(app)
swagger = Swagger(app, template=swagger_template)
jwt = JWTManager(app)

blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypter_token):
    jti = decrypter_token['jti']
    return jti in blacklist

from models import models

# Import endpoints

from resources.external_register import ExternalRegister
from resources.external_login import ExternalLogin

api.add_resource(ExternalRegister, '/api/external/register', endpoint='ext_register')
api.add_resource(ExternalLogin, '/api/external/login', endpoint='ext_login')

# Setup endpoints

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")