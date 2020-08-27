import time
import datetime
import json
import pytz

import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path # this will get you the path variable

import requests



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = os.getenv('GOOGLE_CHROME_SHIM')

def update_data():
    # Get a chrome webdriver (on Mac OSX 'brew cask install chromedriver')
    driver = webdriver.Chrome(executable_path=binary_path, options=chrome_options)
    # Get the webpage for the direct PowerBI visualization from Boston University
    driver.get('https://app.powerbi.com/view?r=eyJrIjoiMzI4OTBlMzgtODg5MC00OGEwLThlMDItNGJiNDdjMDU5ODhkIiwidCI6ImQ1N2QzMmNjLWMxMjEtNDg4Zi1iMDdiLWRmZTcwNTY4MGM3MSIsImMiOjN9')
    driver.implicitly_wait(10)

    # Current date
    current_date = driver.find_elements(By.CLASS_NAME, 'column')[-1].get_attribute('aria-label').split(" ")[1].replace(".", '')
    date = current_date.replace('/', '-')
    date_ts = time.mktime(datetime.datetime.strptime(date, "%m-%d-%y").timetuple())

    # DAILY DATA
    daily_tests_conducted_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[8]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[1]/div[1]'
    daily_tests_pos_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[8]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[3]/div[1]'
    daily_tests_neg_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[8]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[2]/div[1]'
    daily_tests_inv_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[8]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[4]/div[1]'
    avg_sample_process_time_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[17]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div/div[1]'

    daily_tests_conducted = driver.find_element(By.XPATH, daily_tests_conducted_xpath).text
    daily_tests_neg = driver.find_element(By.XPATH, daily_tests_neg_xpath).text
    daily_tests_pos = driver.find_element(By.XPATH, daily_tests_pos_xpath).text
    daily_tests_inv = driver.find_element(By.XPATH, daily_tests_inv_xpath).text
    avg_sample_process_time = driver.find_element(By.XPATH, avg_sample_process_time_xpath).text

    # CUMULATIVE DATA
    cum_title_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[14]/transform/div/div[3]/div/visual-modern/div/svg/g[1]/text/tspan'
    cum_tests_conducted_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[20]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[1]/div[1]'
    cum_tests_neg_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[20]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[2]/div[1]'
    cum_tests_inv_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[20]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[4]/div[1]'
    cum_tests_pos_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[20]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[3]/div[1]'
    cum_avg_sample_process_time_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[18]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div/div[1]'

    cum_tests_conducted = driver.find_element(By.XPATH, cum_tests_conducted_xpath).text
    cum_tests_neg = driver.find_element(By.XPATH, cum_tests_neg_xpath).text
    cum_tests_pos = driver.find_element(By.XPATH, cum_tests_pos_xpath).text
    cum_tests_inv = driver.find_element(By.XPATH, cum_tests_inv_xpath).text
    cum_avg_sample_process_time = driver.find_element(By.XPATH, cum_avg_sample_process_time_xpath).text

    # infected student info
    recovered_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[24]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div/div[1]'
    noncontagious_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[16]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div/div[1]'
    isolated_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[9]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div/div[1]'

    recovered = driver.find_element(By.XPATH, recovered_xpath).text
    noncontagious = driver.find_element(By.XPATH, noncontagious_xpath).text
    isolated = driver.find_element(By.XPATH, isolated_xpath).text

    # Nicely formatted date for daily view
    date_data = driver.find_elements(By.CLASS_NAME, 'card')
    verbose_date = date_data[9].get_attribute("aria-label")
    verbose_date = verbose_date.replace("Latest Result Date ", '')
    verbose_date = verbose_date.replace(".", '')

    daily_tests_conducted = int(daily_tests_conducted.replace(",", ''))
    daily_tests_neg = int(daily_tests_neg.replace(",", ''))
    daily_tests_pos = int(daily_tests_pos.replace(",", ''))
    daily_tests_inv = int(daily_tests_inv.replace(",", ''))

    isolated = int(isolated.replace(",", ''))
    recovered = int(recovered.replace(",", ''))
    noncontagious = int(noncontagious.replace(",", ''))

    cum_tests_conducted = int(cum_tests_conducted.replace(",", ''))
    cum_tests_neg = int(cum_tests_neg.replace(",", ''))
    cum_tests_pos = int(cum_tests_pos.replace(",", ''))
    cum_tests_inv = int(cum_tests_inv.replace(",", ''))

    avg_sample_process_time = float(avg_sample_process_time)
    cum_avg_sample_process_time = float(cum_avg_sample_process_time)

    result =  { date: {
                    'Daily': {
                    'Date_Verbose': verbose_date,
                    'Date_TS': date_ts,
                    'Date': date,
                    'Total': daily_tests_conducted,
                    'Negative': daily_tests_neg,
                    'Positive': daily_tests_pos,
                    'Invalid': daily_tests_inv,
                    'Isolated': isolated,
                    'Recovered': recovered,
                    'Non-Contagious': noncontagious,
                    'Processing Time': avg_sample_process_time
                    },
                'Cumulative': {
                    'Total': cum_tests_conducted,
                    'Negative': cum_tests_neg,
                    'Positive': cum_tests_pos,
                    'Invalid': cum_tests_inv,
                    'Processing Time': cum_avg_sample_process_time
                    }
                }
            }

    driver.quit()

    eastern = pytz.timezone('US/Eastern')
    print(datetime.datetime.now(tz=eastern), "Checking for updates...")

    with open('data.json') as json_file:
        jsonObj = json.load(json_file)
        current_data = jsonObj["data"][-1]
        if list(current_data.keys())[0] == date:
            print(datetime.datetime.now(tz=eastern), "No Change...")
        else:
            print(datetime.datetime.now(tz=eastern), "New Data Added...")
            jsonObj["data"].append(result)
            with open('data.json', 'w') as outfile:
                json.dump(jsonObj, outfile)
            #sendMessages()


def get_ngx(metric="Positive"):
    output_arr = []
    with open('data.json') as json_file:
        covid_data = json.load(json_file)
        for p in covid_data['data']:
            date = list(p.keys())[0]
            m = p[date]["Daily"][metric]
            output_arr.append({"name": date.replace("-", "/"), "value": m})
        return {"data": output_arr}

def get_ngx_all():
    pos_data = get_ngx(metric="Positive")["data"]
    neg_data = get_ngx(metric="Negative")["data"]
    inv_data = get_ngx(metric="Invalid")["data"]
    total_data = get_ngx(metric="Total")["data"]
    multi = [
        {
          "name": "Total",
          "series": total_data
        },
        {
          "name": "Positive",
          "series": pos_data
        },
        {
          "name": "Invalid",
          "series": inv_data
        },
        {
          "name": "Negative",
          "series": neg_data
        }
    ]
    return {"data": multi}
