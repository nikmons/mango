from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, marshal
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from models import models
from utils.security_helper import get_hashed_password

#from resources.fields import employee_fields

class ExternalRegister(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("appl_created", type=str, default="", location='json')
        self.reqparse.add_argument("appl_first_name", type=str, default="", location='json')
        self.reqparse.add_argument("appl_middle_name", type=str, default="", location='json')
        self.reqparse.add_argument("appl_last_name", type=str, default="", location='json')
        self.reqparse.add_argument("appl_father_name", type=str, default="", location='json')
        self.reqparse.add_argument("appl_gender", type=str, default="", location='json')
        self.reqparse.add_argument("appl_date_of_birth", type=str, default="", location='json')
        self.reqparse.add_argument("appl_phone_num", type=str, default="", location='json')
        self.reqparse.add_argument("appl_email", type=str, default="", location='json')
        self.reqparse.add_argument("appl_city", type=str, default="", location='json')
        self.reqparse.add_argument("country_ID", type=str, default="", location='json')
        self.reqparse.add_argument("appl_username", type=str, default="", location='json')
        self.reqparse.add_argument("appl_password", type=str, default="", location='json')

    @swag_from("apidocs/external_register.yml")
    def post(self):
        args = self.reqparse.parse_args()
        print(args)
        chk_ext_user = models.Applicants.query.filter_by(appl_username=args["appl_username"]).first()
        print("Existing user = {}".format(chk_ext_user))

        if chk_ext_user is not None:
            return {"message" : "User '{}' already exists".format(args["appl_username"])}, 400

        ext_user = models.Applicants(
            appl_first_name = args["appl_first_name"],
            appl_middle_name = args["appl_middle_name"],
            appl_last_name = args["appl_last_name"],
            appl_father_name = args["appl_father_name"],
            appl_gender = args["appl_gender"],
            appl_date_of_birth = args["appl_date_of_birth"],
            appl_phone_num = args["appl_phone_num"],
            appl_email = args["appl_email"],
            appl_city = args["appl_city"],
            country_ID = args["country_ID"],
            appl_username = args["appl_username"],
            appl_password = get_hashed_password(args["appl_password"])
        )

        print(type(get_hashed_password(args["appl_password"])))
        print(args["appl_password"])
        print(ext_user.appl_password)
        print(type(ext_user.appl_password))

        db.session.add(ext_user)
        db.session.commit()