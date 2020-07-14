from selenium import webdriver
import time

class getText():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        element = driver.find_element_by_id("opentab")
        elementText = element.text
        print("Text on the element is: " +elementText)
        time.sleep(2)
        driver.quit()


ff = getText()
ff.test()

