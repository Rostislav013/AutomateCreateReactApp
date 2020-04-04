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


def create():
    folderName = str(sys.argv[1])
    driver.get("https://github.com/login/")
    login = driver.find_element_by_id("login_field")
    login.send_keys(username)
    password_input = driver.find_element_by_id("password")
    password_input.send_keys(password)
    sigin = driver.find_element_by_name("commit")
    sigin.click()
    driver.get("https://github.com/new")
    repo_input = driver.find_element_by_id("repository_name")
    repo_input.send_keys(folderName)
    createButton = driver.find_element_by_xpath(
        "//button[contains(text(),'Create repository')]")
    createButton.submit()
    driver.quit()
    print("Repository was created {}".format(folderName))


if __name__ == "__main__":
    create()
