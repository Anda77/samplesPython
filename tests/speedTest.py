from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = ' #your email'
TWITTER_PASSWORD = '#your password'

CHROME_DRIVER_PATH = "C:\\PythonPrj\\drivers\\chromedriver110.exe"
s = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=s)
URL = 'https://www.speedtest.net/'
driver.get(URL)
sleep(2)
