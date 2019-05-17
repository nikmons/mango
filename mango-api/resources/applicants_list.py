from flask import Flask, jsonify, abort, make_response, session
from flask_restful import Api, Resource, reqparse, marshal
from flasgger import swag_from
from utils.secure_creds import check_password

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from werkzeug.security import safe_str_cmp

from app import db, jwt
from models import models

import datetime

class ExternalLogin(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(ExternalLogin, self).__init__()

    @swag_from("apidocs/external_login.yml")
    def post(self):
