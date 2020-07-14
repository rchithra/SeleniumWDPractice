from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class JavascriptExecution():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.execute_script("window.location =  'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(3)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

ff = JavascriptExecution()
ff.test()