from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Users\IT Lab\Desktop\driver\chromedriver')
driver.get('http://puzzlepedia.esy.es/project/login.php');

username = driver.find_element_by_id("email")
username.send_keys("rlbagad2@gmail.com")
driver.find_element_by_name("data").click()

time.sleep(5) 
driver.quit()