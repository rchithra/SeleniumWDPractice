from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys:

    def test(self):
        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        loginlink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginlink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")

        time.sleep(2)

        driver.close()

ff = ClickAndSendKeys()
ff.test()
