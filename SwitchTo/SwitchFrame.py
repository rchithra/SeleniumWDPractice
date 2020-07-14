from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchtoFrame():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.execute_script("window.scrollBy(0,1000);")

        # Switch to frame using id
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using number
        # driver.switch_to.frame(0)

        time.sleep(2)
        driver.find_element(By.ID, "search-courses").send_keys("python")
        time.sleep(2)

        # Switch to parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000;")
        driver.find_element(By.ID, "name").send_keys("Test Successful")
