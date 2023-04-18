import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\PythonPrj\\drivers\\chromedriver110.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# Connect to Tinder.com
url = "https://tinder.com/"
driver.get(url)

ACCOUNT_EMAIL = "andadeacu@yahoo.com"
ACCOUNT_PASSWORD = "Rucar#2525"
time.sleep(5)
# Accept Cookies
accept_cookies = driver.find_element('//*[@id="u-648818393"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()

login_button = driver.find_element('//*[@id="u-648818393"]/div/div[1]/div/main/div['
                                   '1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(5)
# Avoid mobile mode !
driver.maximize_window()
base_window = driver.window_handles[0]
print(driver.title)
accept_in = driver.find_element('//*[@id="u1917767827"]/div/div/div[1]/div/div[3]/span/div[2]/button')
accept_in.click()

# Enter to Facebook Dialog !
time.sleep(5)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Waiting for Cookies!
time.sleep(5)
accept_cookies_facebook = driver.find_elements_by_css_selector("button")
accept_cookies_facebook[1].click()

# Start to log in :
email_field = driver.find_element("email")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element("pass")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
