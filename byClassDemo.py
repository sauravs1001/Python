from selenium import webdriver
from selenium.webdriver.common.by import By


class ByClassDemo:
    def test(self):
        baseURL1 = "https://letskodeit.teachable.com/p/practice"
        driver =webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.get(baseURL1)
        driver.maximize_window()
        driver.implicitly_wait(30)

        elementByID = driver.find_element(By.ID, "name")

        if elementByID is not None:
            print("Found one element using By class ID")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("Found one element using By class XPATH")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("Found one element using By class Link text")


obj2 = ByClassDemo()
obj2.test()



