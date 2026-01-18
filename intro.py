# Microsoft Edge Setup for Selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path=r"C:\Users\Shobe\Desktop\Automation\msedgedriver.exe")  # Specify the path to Edge WebDriver
driver = webdriver.Edge(service=service)

# This file practices basic Selenium operations such as opening a webpage,
# locating elements, and interacting with them.
driver.get("https://www.google.com") # Open Google homepage
time.sleep(10)  # Wait for the page to load
driver.quit()

