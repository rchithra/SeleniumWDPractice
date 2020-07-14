from selenium import webdriver
import time


class getAttribute():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")

        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()


ff = getAttribute()
ff.test()
