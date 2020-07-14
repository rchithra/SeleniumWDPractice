from selenium import webdriver

class RunFFtest():
    def testmethod(self):
        #driver = webdriver.Firefox(executable_path="C:\\Users\\My PC\\workspace_python\\drivers\\geckodriver.exe")
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")

ff = RunFFtest()
ff.testmethod()



