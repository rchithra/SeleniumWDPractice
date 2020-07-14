from selenium import webdriver
import time

class AutoComplete():

    def test(self):
        baseUrl = "http://www.southwest.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        cityField.send_keys("New York")
        time.sleep(2)
        itemtoSelect = driver.find_elements_by_xpath("")
        itemtoSelect.click()
        time.sleep(2)
        driver.quit()

ff = AutoComplete()
ff.test()

