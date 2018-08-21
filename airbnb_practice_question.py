from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AirBNB:
    def test_airbnb_home_page(self):
        base_url = "https://www.cleartrip.com/"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(base_url)

        


obj_air = AirBNB()
obj_air.test_airbnb_home_page()