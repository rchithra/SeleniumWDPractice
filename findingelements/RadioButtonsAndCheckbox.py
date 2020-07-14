from selenium import webdriver
import time

class RadioButtonAndCheckboxes():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        bmwradiobtn = driver.find_element_by_id("bmwradio")
        bmwradiobtn.click()

        time.sleep(2)
        benzradiobtn = driver.find_element_by_id("benzradio")
        benzradiobtn.click()

        time.sleep(2)
        hondaradiobtn = driver.find_element_by_id("hondaradio")
        hondaradiobtn.click()

        time.sleep(2)
        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)
        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()

        time.sleep(2)
        hondaCheckbox = driver.find_element_by_id("hondacheck")
        hondaCheckbox.click()

        print("BMW radio button is selected?:" + str(bmwradiobtn.is_selected()))
        print("Benz radio button is selected?:" + str(benzradiobtn.is_selected()))
        print("Honda radio button is selected?:" + str(hondaradiobtn.is_selected()))
        print("BMW checkbox is selected?:" + str(bmwCheckbox.is_selected()))
        print("Benz checkbox is selected?:" + str(benzCheckbox.is_selected()))
        print("Honda checkbox is selected?:" + str(hondaCheckbox.is_selected()))

        time.sleep(2)
        driver.close()



ff = RadioButtonAndCheckboxes()
ff.test()



