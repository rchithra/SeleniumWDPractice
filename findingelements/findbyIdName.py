from selenium import webdriver


class FindbyIdName():
    def test(self):
        baseUrl = "https://accounts.google.com/signup"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyId = driver.find_element_by_id("firstName")
        if elementbyId is not None:
            print("Found an element by Id")

        elementbyName = driver.find_element_by_name("lastName")
        if elementbyName is not None:
            print("Found an element by Name")


ff = FindbyIdName()
ff.test()
