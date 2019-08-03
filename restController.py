from flask import Flask
from flask_restful import Resource, Api
import tfSentenseEncoder as tf

app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def post(self, messages):
        return tf.embed(messages)


api.add_resource(Employees, '/encoder')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')