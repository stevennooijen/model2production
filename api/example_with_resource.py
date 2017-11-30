import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("user_id", type=str)


class Predict(Resource):
    def __init__(self, *args, **kwargs):
        super(Predict, self).__init__(*args, **kwargs)
        self.model = None
        self.load_model()

    def get(self):
        arguments = parser.parse_args()
        result = {
            'probability': 0.5,
            'label': 1.,
            'user_id': arguments['user_id'],
            "model" : self.model
        }
        return jsonify(**result)

    def load_model(self):
        self.model = "My complex model"
        return "Great success loading model"


api.add_resource(Predict, '/api/v1/predict')

if __name__ == '__main__':
    app.run(host='18.195.167.46', debug=True, port=5000)