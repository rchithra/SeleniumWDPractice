from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat():

    def test(self):
        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)

        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("rchithra181@gmail.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("test123")
        driver.find_element(By.NAME, "commit").click()

        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")

        _course = "//div[contains(@class , 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(2)
        driver.quit()

ff = DynamicXpathFormat()
ff.test()

