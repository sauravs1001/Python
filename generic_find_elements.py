from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HandyWrapperClass:
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locator = locatorType.lower()
        if locator == "id":
            return By.ID

        elif locator == "xpath":
            return By.XPATH

        else:
            print("Locator type is not supported")

        return False





