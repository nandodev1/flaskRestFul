from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

input = open("data.json")
data = json.load(input)

print(data)