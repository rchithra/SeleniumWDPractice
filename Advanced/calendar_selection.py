from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CalendarSelection():

    def test(self):
        baseUrl = "https://www.expedia.com.sg/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        driver.find_element_by_id("tab-flight-tab-hp").click()
        departingField = driver.find_element_by_id("flight-departing-hp-flight")
        departingField.click()
        datatoSelect = driver.find_elements_by_xpath()
        datatoSelect.click()
        time.sleep()
        driver.quit()

    def test2(self):
        baseUrl = "https://www.expedia.com.sg/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        driver.find_element_by_id("tab-flight-tab-hp").click()
        departingField = driver.find_element_by_id("flight-departing-hp-flight")
        departingField.click()
        calmonth = driver.find_elements_by_xpath("//div[@class = 'datepicker-cal-month'][1]")
        allValidDates = calmonth.find_elements(By.TAG_NAME, "button")

        time.sleep(5)
        for date in allValidDates:
            if date.text == "30":
                break


ff = CalendarSelection()
ff.test()
ff.test2()
