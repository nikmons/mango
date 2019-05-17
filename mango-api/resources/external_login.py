from flask import Flask, jsonify, abort, make_response, session
from flask_restful import Api, Resource, reqparse, marshal
from flasgger import swag_from
from utils.security_helper import check_password

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
        args = self.reqparse.parse_args()
        ext_user =  models.Applicants.query.filter_by(appl_username = str(args['username'])).first()
        print(args)
        if ext_user and check_password(args['password'], ext_user.appl_password):
            expires = datetime.timedelta(days=20)
            access_token = create_access_token(
                identity=ext_user.appl_id, fresh=True, expires_delta=expires)
            refresh_token = create_refresh_token(ext_user.appl_id)

            # login_entry = models.Employees_Logins(Emp_id=user.Emp_id)
            # db.session.add(login_entry)
            # db.session.commit()

            return {
                'message':'user_authenticated',
                'ext_user':args['username'],
                'ext_user_id': ext_user.appl_id,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {"message": "Invalid Credentials!"}, 401