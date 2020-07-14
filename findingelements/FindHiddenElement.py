from selenium import webdriver
import time

class HiddenElements():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        #Find the stste of textbox
        textboxElement = driver.find_element_by_id("displayed-text")
        textboxState = textboxElement.is_displayed()
        print("Text box visible ?: "+str(textboxState))
        time.sleep(2)

        #Click the hide button
        driver.find_element_by_id("hide-textbox").click()
        #Find state of textbox
        textboxState = textboxElement.is_displayed()
        print("Text box visible ?: " + str(textboxState))
        time.sleep(2)

        #Click show button
        driver.execute_script("window.scrollBy(0,-150)")
        driver.find_element_by_id("show-textbox").click()
        textboxState = textboxElement.is_displayed()
        print("Text box visible ?: " + str(textboxState))
        time.sleep(2)
        driver.quit()



ff = HiddenElements()
ff.test()





