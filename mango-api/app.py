from flask import Flask, jsonify, abort, make_response, render_template
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")