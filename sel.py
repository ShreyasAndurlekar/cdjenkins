from selenium import webdriver  # Lowercase "s" in "selenium"
import time
from selenium.webdriver.common.keys import Keys  # Lowercase "s" in "selenium"

print("Sample test case started")

# Set up ChromeDriver (Make sure ChromeDriver is in PATH or provide full path)
driver = webdriver.Chrome()  

# Maximize the window
driver.maximize_window()

# Navigate to Google
driver.get("https://www.google.com/")

# Locate the Google search box and enter a search term
search_box = driver.find_element("name", "q")  # Updated method
search_box.send_keys("What is Docker")

time.sleep(2)  # Small delay

# Press ENTER to search
search_box.send_keys(Keys.ENTER)

time.sleep(3)  # Wait for results to load

# Close the browser
driver.close()

print("Sample test case successfully completed")

