#!flask/bin/python
from os import abort

from flask import Flask, jsonify
from apps.data_loaders.load_data import DataLoader

app = Flask(__name__)
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


@app.route('/config-prediction/api/v1.0/service-data/all-data', methods=['GET'])
def get_all_data():
    dataLoader.get_all_data("", "")
    return jsonify({'tasks': tasks})


@app.route('/config-prediction/api/v1.0/service/config-data', methods=['GET'])
def get_config_data():
    return jsonify({'tasks': tasks})


@app.route('/config-prediction/api/v1.0/service/reliability-data', methods=['GET'])
def get_reliability_data():
    return jsonify({'tasks': tasks})


@app.route('/config-prediction/api/v1.0/service/efficiency', methods=['GET'])
def get_efficiency_data():
    return jsonify({'tasks': tasks})


@app.route('/config-prediction/api/v1.0/service/retention-data', methods=['GET'])
def get_retention_data():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
