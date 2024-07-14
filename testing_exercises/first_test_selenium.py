from selenium import webdriver
import time

def openChrome():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    return driver

# Example usage
driver = openChrome()
while True:
    pass

