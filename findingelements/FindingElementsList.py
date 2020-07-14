from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementsList():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        radioButtonlist = driver.find_elements(By.XPATH, "//input[contains(@type,'radio')and contains(@name,'cars')]")
        size = len(radioButtonlist)
        print("Size of the radio button list:" + str(size))

        for radiobutton in radioButtonlist:
            isSelected = radiobutton.is_selected()

            if not isSelected:
                radiobutton.click()
                time.sleep(2)


ff = ElementsList()
ff.test()
