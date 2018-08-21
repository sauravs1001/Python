from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from getpass import getpass
import time


class IFrames:
    def test_iframes(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.execute_script("window.scrollBy(0, 1000);")

        driver.switch_to.frame("courses-iframe")
        driver.find_element(By.ID, "search-courses").send_keys("python", Keys.RETURN)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -1000);")

        driver.switch_to.default_content()
        driver.find_element(By.ID, "name").send_keys("Test passed")

        # driver.switch_to.alert.accept()
        # driver.switch_to.alert.dismiss()




        driver.close()






obj = IFrames()
obj.test_iframes()
