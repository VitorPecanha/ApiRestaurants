from flask import Flask
from flask_restful import Resource, Api, reqparse
from numpy import require
import pandas as pd
import ast

class Users(Resource):
    def get(self):
        data = pd.read_csv('ApiRestaurants/users.csv')
        return {'data': data.to_dict()}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('userId', require=True)
        parser.add_argument('name', require=True)
        parser.add_argument('city', require=True)

        args = parser.parse_args()

        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name' : args['name'],
            'city ' : args['city'],
            'locations' : [[]]
        })

        data = pd.read_csv('ApiRestaurants/users.csv')
        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200

class Locations(Resource):
    def get(self):
        data = pd.read_csv('ApiRestaurants/locations.csv')
        data = data.to_dict()
        return {'data': data}, 200

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()