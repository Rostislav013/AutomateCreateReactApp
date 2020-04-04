import sys
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
load_dotenv()
username = os.getenv("user")
password = os.getenv("password")
firefox_path = os.getenv("driver_path")
driver = webdriver.Firefox(firefox_path)


driver.get("https://github.com/login/")
login = driver.find_element_by_id("login_field")
login.send_keys(username)
password_input = driver.find_element_by_id("password")
password_input.send_keys(password)
sigin = driver.find_element_by_name("commit")
sigin.click()
driver.get("https://github.com/new")

print("Succesfully created repository")
