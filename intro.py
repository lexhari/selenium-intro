# Microsoft Edge Setup for Selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=r"C:\Users\Shobe\Desktop\Automation\msedgedriver.exe")  # Specify the path to Edge WebDriver
driver = webdriver.Edge(service=service)

# This file practices basic Selenium operations such as opening a webpage,
# locating elements, and interacting with them.
driver.get("https://www.google.com") # Open Google homepage

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")  # Locate the search input box by its name attribute ; look for the first element with class name 'gLFyf'
input_element.send_keys("hotdog" + Keys.ENTER)  # send_keys to input text into the search box

time.sleep(10)  # Wait for the page to load
driver.quit()

