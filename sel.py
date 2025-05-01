from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("Sample test case started")

driver = webdriver.Chrome()  
driver.maximize_window()

driver.get("https://www.google.com/")

search_box = driver.find_element("name", "q")
search_box.send_keys("What is Docker")

time.sleep(2)

search_box.send_keys(Keys.ENTER)

time.sleep(3)

driver.close()

print("Sample test case successfully completed")
