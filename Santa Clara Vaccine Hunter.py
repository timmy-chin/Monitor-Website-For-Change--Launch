from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from datetime import datetime

for number in range(50):
    source = requests.get('https://vax.sccgov.org/mvcc').text
    soup = BeautifulSoup(source, 'lxml')
    div = soup.find('div')
    headline1 = div.h3.span.text

    time.sleep(600)

    source = requests.get('https://vax.sccgov.org/mvcc').text
    soup = BeautifulSoup(source, 'lxml')
    div = soup.find('div')
    newheadline1 = div.h3.span.text


    if headline1 == newheadline1:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("No Change  ", current_time)


    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print('Something Changed!  ', current_time)
        browser = webdriver.Chrome('/Users/joannelee/Downloads/chromedriver')
        browser.get('https://vax.sccgov.org/mvcc')
        break



