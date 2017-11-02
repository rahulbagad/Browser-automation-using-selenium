from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('path-to-chromedriver')
driver.get('http://example.com/');

username = driver.find_element_by_id("email")
username.send_keys("email")
username = driver.find_element_by_id("password")
username.send_keys("pass@123")
driver.find_element_by_name("data").click()

time.sleep(5) 
driver.quit()
