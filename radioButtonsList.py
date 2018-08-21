from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class RadioButtonList:
    def radioButtobList(self):
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        baseURL = "https://www.makemytrip.com"
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(12)
        rdBtnList = driver.find_elements(By.XPATH, "//input[@type= 'radio']")
        print(len(rdBtnList))
        for i in rdBtnList:
            print(i.is_displayed())



rd = RadioButtonList()
rd.radioButtobList()
