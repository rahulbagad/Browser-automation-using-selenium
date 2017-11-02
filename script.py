from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('path-to-chromedriver')
driver.get('https://github.com/login');

username = driver.find_element_by_id("login_field")
username.send_keys("username")

username = driver.find_element_by_id("password")
username.send_keys("pass123")

driver.find_element_by_name("commit").click()

time.sleep(5) 
driver.quit()
