from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = None
try:
    cpath = "C:\\NATALY\\Python\\Util\\chromedriver.exe"
    driver = webdriver.Chrome(cpath)
    driver.get("https://stackoverflow.com/users/login")
    e = driver.find_element(By.NAME, "email")
    e.send_keys("") #stackoverflow email to login
    e = driver.find_element(By.NAME, "password")
    e.send_keys("")  # stackoverflow password to login
    e = driver.find_element(By.ID, "submit-button")
    e.click()
    time.sleep(3)
    driver.save_screenshot("result.png") # will create result image in the same folder

finally:
    if driver is not None:
        driver.close()