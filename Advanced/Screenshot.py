from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshot():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        driver.find_element(By.ID, "user_email").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        destinationScreenshot = "C:\\Users\\My PC\\Desktop\\test.png"

        try:
            driver.save_screenshot(destinationScreenshot)
            print("Screenshot saved to directory: " + destinationScreenshot)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshot()
ff.test()
