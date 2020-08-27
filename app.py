
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
from data_fetcher import update_data, get_ngx

# Flask Config
app = Flask(__name__)
api = Api(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Schedule the data update
sched = BackgroundScheduler(daemon=True)
sched.add_job(update_data,'interval',minutes=15)
sched.start()

@app.route("/all", methods=['GET'])
def all():
    with open('data.json') as json_file:
        jsonObj = json.load(json_file)
        return jsonObj

@app.route("/current", methods=['GET'])
def current():
    with open('data.json') as json_file:
        jsonObj = json.load(json_file)
        return jsonObj["data"][-1]

@app.route("/ngx", methods=['GET'])
def ngx():
    return get_ngx(metric="Positive")

if __name__ == "__main__":
    app.run()
