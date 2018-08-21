from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from getpass import getpass


class GetTextAttribute:
    def test_text_other_attribute(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(base_url)

        element = driver.find_element(By.ID, "carselect")
        print(element.text)
        print(element.get_attribute("name"))

        element1 = driver.find_element_by_id("openwindow")
        print(element1.text)
        print(element1.get_attribute("class"))



obj = GetTextAttribute()
obj.test_text_other_attribute()