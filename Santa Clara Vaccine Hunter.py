# This program works by monitoring a sentence or word (ie. no appointment or unavailable) on a website. If the sentence or word remains the same after a certain time, it will continue to monitor. If the sentence or word changes, it will launch the website
# To use these codes, install beautifulsoup by typing "pip install bs4" in your terminal. 
# Then, install requests by typing "pip install requests" in your terminal
# Then, install lxml by typing "pip install lxml" in your terminal
# To enable the launching feature, install selenium by typing "pip install selenium" in your terminal
# Go to https://chromedriver.chromium.org/downloads, download the chromedriver that matches your current chrome version. Open the file location and copy that location for your first variable


from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from datetime import datetime

# Paste your chromedriver location down here
Chromedriverlocation = input("Chromedriver file location:")

# Which website do you want to monitor
website = input("Website URL:")

# How often do you want to check the website for change? Type it in seconds (ie. 5 minutes = 300)
checkingtime = input("Check for Update every (in seconds):")

# For how long do you want this program to be monitoring the website? Type it in hours (ie. 1 hour = 1)
monitoringtime = input("Run this program for (in hours):")

tagname = input('tagname that surrounds word or phrase:')

workingtime = 3600 * int(monitoringtime) / int(checkingtime)

# calculate working time and insert it below if error occurs
for number in range(int(workingtime)):
    # This part is tricky, paste these 4 lines of code into a separate python file to find your changing word
    source = requests.get(website).text
    soup = BeautifulSoup(source, 'lxml')
    # Find out what are the tags that surround the word you want to monitor (ie. if the tag for your word is div, type div below)
    word = soup.find(tagname)
    # Find out what are the more specific tags surrounding the word you want to monitor (ie. if you see h3 and span, type word.h3.span.text)
    headline = word.text
    # Use print(headline) to check if you got the right word. If not, keep trying to get the word by changing tag names that surrounds the word until you get the right word printed
    # Once you got the right word, copy paste all 4 lines back here

    time.sleep(int(checkingtime))

    # Copy paste the 4 lines of code here too, but change headline to newheadline, you should be able to run it by now.
    source = requests.get(website).text
    soup = BeautifulSoup(source, 'lxml')
    word = soup.find(tagname)
    newheadline = word.text

    if headline == newheadline:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("No Change  ", current_time)


    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print('Something Changed!  ', current_time)
        browser = webdriver.Chrome(Chromedriverlocation)
        browser.get(website)
        break




