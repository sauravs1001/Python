from selenium import webdriver
from selenium.webdriver.common.by import By


class HiddenElements:
    def test_hiddenControls(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)

        driver.get(baseURL)


obj = HiddenElements()
obj.test_hiddenControls()
