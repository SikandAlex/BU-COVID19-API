
from flask import Flask, g
from flask_restful import Api, Resource, reqparse
from apscheduler.schedulers.background import BackgroundScheduler

import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Custom function to grab new data from Healthway dashboard
from data_fetcher import update_data, get_ngx, get_ngx_all


from flask_cors import CORS, cross_origin





update_data()

# Flask Config
app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

# Schedule the data update
sched = BackgroundScheduler(daemon=True)
sched.add_job(update_data,'interval',minutes=15)
sched.start()

@app.route("/all", methods=['GET'])
@cross_origin()
def all():
    with open('data.json') as json_file:
        jsonObj = json.load(json_file)
        return jsonObj

@app.route("/current", methods=['GET'])
@cross_origin()
def current():
    with open('data.json') as json_file:
        jsonObj = json.load(json_file)
        return jsonObj["data"][-1]

@app.route("/ngx/<string:metric>", methods=['GET'])
@cross_origin()
def ngx(metric):
    return get_ngx(metric=metric)

@app.route("/ngx-all", methods=['GET'])
@cross_origin()
def ngx_all():
    return get_ngx_all()

@app.route("/ngx-infections", methods=['GET'])
@cross_origin()
def ngx_infections():
    with open('data.json') as json_file:
        jsonObj = json.load(json_file)
        key = list(jsonObj["data"][-1].keys())[0]
        current = jsonObj["data"][-1][key]["Daily"]
        print(current)
        return {"data": [{"name": "Isolated", "value": current["Isolated"]}, {"name": "Non-Contagious", "value": current["Non-Contagious"]}, {"name": "Recovered", "value": current["Recovered"]}]}


if __name__ == "__main__":
    app.run()
