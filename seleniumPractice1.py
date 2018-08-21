from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RunChromeTest:

    def test(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        practice_page = driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        driver.implicitly_wait(30)
        print(driver.title)
        elementbyId = driver.find_element_by_id("name")

        if elementbyId is not None:
            print("Found one element by id")

        elementbyName = driver.find_element_by_name("show-hide")

        if elementbyName is not None:
            print("Found other element by name")
        # search_field.clear()
        # search_field.send_keys("Python" + Keys.RETURN)


chromtest = RunChromeTest()
chromtest.test()





