# import Flask and jsonify
from flask import Flask, jsonify, request

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

# import pandas, numpy, pickle
import pandas as pd
import numpy
import pickle

#definitions
app = Flask(__name__)    
api = Api(app)

model = pickle.load(open('model.p', 'rb'))

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        
        #Make predictions
        res = model.predict(df)
        return res.tolist()
    
#Make endpoint
api.add_resource(Scoring, '/scoring')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4242', debug=True)