from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

input = open("data.json")
data = json.load(input)

hospital = data['hospital']
services = data['services']
complaint = data['complaint']

class Services(Resource):
  def get(self):
    return {'services' : services}

class Complaints(Resource):
  def get(self):
    return {'complaints':complaint}
  
  def post(self):
    complaint.append(
      {
        'name':request.json['name'],
        'email':request.json['email'],
        'contact':request.json['contact'],
        'description':request.json['description']
      }
    )

    return {'status': 'sucefull'}