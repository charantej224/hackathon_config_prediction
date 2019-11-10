#!flask/bin/python
from os import abort

from flask import Flask, jsonify
from apps.data_loaders.load_data import DataLoader
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
dataLoader = DataLoader()

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/config-prediction/api/v1.0/service/all-data', methods=['GET'])
def get_all_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    # return dataLoader.get_all_data("9/9/19 18:57", "11/4/19 21:59")
    return dataLoader.get_all_data(start_time, end_time)


@app.route('/config-prediction/api/v1.0/service/config-data', methods=['GET'])
def get_config_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    return dataLoader.get_all_config_data(start_time, end_time)


@app.route('/config-prediction/api/v1.0/service/reliability-data', methods=['GET'])
def get_reliability_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    return dataLoader.get_reliability_info(start_time, end_time)


@app.route('/config-prediction/api/v1.0/service/efficiency', methods=['GET'])
def get_efficiency_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    return dataLoader.get_efficiency_data(start_time, end_time)


@app.route('/config-prediction/api/v1.0/service/retention', methods=['GET'])
def get_retention_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    return dataLoader.get_retention_data(start_time, end_time)


if __name__ == '__main__':
    app.run(debug=True)
