from selenium import webdriver


class FindbyXpathCss():
    def test(self):
        baseUrl = "https://accounts.google.com/signup"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyXpath = driver.find_element_by_xpath("//input[@id='firstName']")
        if elementbyXpath is not None:
            print("Found an element by Xpath")

        elementbyCss = driver.find_element_by_css_selector()
        if elementbyCss is not None:
            print("Found an element by Name")


ff = FindbyXpathCss()
ff.test()
