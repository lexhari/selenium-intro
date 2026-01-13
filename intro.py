# Microsoft Edge Setup for Selenium
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service

service = Service(executable_path=r"C:\Users\Shobe\Desktop\Automation\msedgedriver.exe")  # Specify the path to Edge WebDriver
driver = webdriver.Edge(service=service)

# This file practices basic Selenium operations such as opening a webpage,
# locating elements, and interacting with them.
driver.get("https://www.bing.com")


