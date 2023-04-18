import time

from selenium import webdriver

EMAIL_ACCOUNT = "andadeacu@yahoo.com"
EMAIL_PASSWORD = "Rucar#2525"

chrome_driver_path = "C:\\PythonPrj\\drivers\\chromedriver110.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
driver.maximize_window()
main_page = driver.current_window_handle

time.sleep(5)
login_button = driver.find_element_by_xpath(
    '//*[@id="q-2110398392"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(5)
fb_account_login = driver.find_element_by_xpath('//*[@id="q456187828"]/div/div/div[1]/div/div[3]/span/div[2]')
fb_account_login.click()
