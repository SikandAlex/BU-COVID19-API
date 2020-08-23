from firebase import firebase
from flask import Flask
from flask_restful import Api, Resource, reqparse
from apscheduler.schedulers.background import BackgroundScheduler

import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Custom function to grab new data from Healthway dashboard
from data_fetcher import update_data

# Firebase config
firebase_url = "https://bu-covid-19-dashboard.firebaseio.com/"
firebase_app = firebase.FirebaseApplication(firebase_url, None)

# Flask Config
app = Flask(__name__)
api = Api(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Schedule the data update
sched = BackgroundScheduler(daemon=True)
sched.add_job(update_data,'interval',minutes=15)
sched.start()

@app.route("/home", methods=['GET'])
def home():
    return "Welcome to the BU COVID-19 API! \n Created by Alex Sikand"

@app.route("/current", methods=['GET'])
def current():
    result = firebase_app.get('/current', 'current')
    return result

@app.route('/historical', methods=['GET'])
def get_historical(date):
    result = firebase_app.get('/reporting', '')#.items()
    return result

if __name__ == "__main__":
    app.run()
