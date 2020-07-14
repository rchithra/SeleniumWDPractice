import time
from selenium import webdriver
from Utilities.handy_wrappers import HandyWrappers


class UsingWrappers1():
    def test(self):

        baseurl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseurl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id ='name']", locatorType="xpath")
        textField2.send_keys("test2")
        time.sleep(2)
        textField2.clear()
        driver.quit()


ff = UsingWrappers1()
ff.test()
