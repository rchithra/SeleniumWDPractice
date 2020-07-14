from selenium import webdriver
class Chromedrivers:
    def testmethod(self):
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(executable_path="C:\\Users\\My PC\\workspace_python\\drivers\\chromedriver.exe")
        driver.get("http://www.letskodeit.com")



CC= Chromedrivers()
CC.testmethod()



