from flask_restful import Resource
from app import api

class HelloWorld(Resource):
    def get(self):
        data={"data":"Hello World"}
        return data

api.add_resource(HelloWorld,'/hello')
