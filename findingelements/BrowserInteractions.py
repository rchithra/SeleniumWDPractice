from selenium import webdriver


class BrowserInteractions:

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()

        # windows maximize
        driver.maximize_window()
        # open the url
        driver.get(baseurl)
        # get title
        title = driver.title
        print("Title of the webpage is: " + title)
        # get current url
        current_url = driver.current_url
        print("Current_url of the web page is: " + current_url)
        # browser refresh
        driver.refresh()
        print("Browser refreshed first time")
        driver.get(driver.current_url)
        print("Browser refreshed second time")
        # open another url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        current_url = driver.current_url
        print("Current url of the webpage is:" + current_url)
        # Browser back
        driver.back()
        print("Go one step back in browser history")
        current_url = driver.current_url
        print("Current url of the page is : " + current_url)
        # Browser forward
        driver.forward()
        print("Go one step forward in the browser history")
        current_url = driver.current_url
        print("Current url of the page is : " + current_url)
        # Get Page source
        PageSource = driver.page_source
        print(PageSource)
        # Browser close/quit
        # driver.close()
        driver.quit()


ff = BrowserInteractions()
ff.test()
