from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class ExplicitWaitDemo():

    def test(self):
        baseUrl = "http://www.expedia.sg"
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("01/06/2020")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        time.sleep(2)
        returnDate.send_keys("02/07/2020")
        driver.find_element(By.LINK_TEXT, "Search").click()

ff = ExplicitWaitDemo()
ff.test()
