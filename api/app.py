import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from sklearn.externals import joblib
import pandas as pd


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("sample_uuid", type=str)
# add features for model
for feature in ['user_age', 'body_length', 'channels']:
    parser.add_argument(feature, type=int)


class Predict(Resource):
    def __init__(self, *args, **kwargs):
        super(Predict, self).__init__(*args, **kwargs)
        self.model_file = 'api/model.pkl'
        self.load_model()

    def get(self):
        arguments = parser.parse_args()
        # transform to pandas and remove user id
        arguments_df = pd.DataFrame.from_dict(arguments, orient='index').T
        arguments_df.pop('sample_uuid')
        result = {
            'probability': self.model.predict_proba(arguments_df)[0, 1],
            'label': int(self.model.predict(arguments_df)[0]),
            'sample_uuid': arguments['sample_uuid'],
        }
        return jsonify(**result)

    def load_model(self):
        self.model = joblib.load(self.model_file)
        return self


api.add_resource(Predict, '/api/v1/predict')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)