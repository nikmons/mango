from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, marshal
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from models import models
from utils.security_helper import get_hashed_password

#from resources.fields import employee_fields

class CountriesListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('COUNTRY_ISO_CODE', type=str, default="",
                                    location='json')
        self.reqparse.add_argument('COUNTRY_NAME', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('COUNTRY_STATE_NAME', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('COUNTRY_PHONE_CODE', type=str, default="",
                                   location='json')

        super(CountriesListAPI, self).__init__()


    @jwt_required
    #@swag_from("apidocs/devices_post.yml")
    def post(self):
        args = self.reqparse.parse_args()
        print(args)
        country = models.Devices(country_iso_code=args["COUNTRY_ISO_CODE"],
                                    country_name=args["COUNTRY_NAME"], country_state_name=args["COUNTRY_STATE_NAME"],
                                    country_phone_code=args["COUNTRY_PHONE_CODE"])
        db.session.add(country)
        db.session.commit()