from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHovering():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        element = driver.find_element(By.ID,"mousehover")
        itemtoClicklocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print ("Mouse hovered")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH,itemtoClicklocator)
            actions.move_to_element(topLink).click().perform()
            print("Item clicked")
        except:
            print("Mouse Hover failed on element")

ff = MouseHovering()
ff.test1()