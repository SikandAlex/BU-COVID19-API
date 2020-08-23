from firebase import firebase
firebase_url = "https://bu-covid-19-dashboard.firebaseio.com/"
firebase_app = firebase.FirebaseApplication(firebase_url, None)

import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = GOOGLE_CHROME_PATH


def update_data():
    # Get a chrome webdriver (on Mac OSX 'brew cask install chromedriver')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    # Get the webpage for the direct PowerBI visualization from Boston University
    driver.get('https://app.powerbi.com/view?r=eyJrIjoiMzI4OTBlMzgtODg5MC00OGEwLThlMDItNGJiNDdjMDU5ODhkIiwidCI6ImQ1N2QzMmNjLWMxMjEtNDg4Zi1iMDdiLWRmZTcwNTY4MGM3MSIsImMiOjN9')
    driver.implicitly_wait(10)

    # Current date
    current_date = driver.find_elements(By.CLASS_NAME, 'column')[6].get_attribute('aria-label').split(" ")[2].replace(".", '')
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

    data =  { 'Daily': {
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

    driver.quit()

    result = firebase_app.put('/reporting', date, data)
    current = firebase_app.put('/reporting', 'current', data)
    print("LOGGED: ", result)
