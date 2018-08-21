from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from getpass import getpass
import time


class SwitchWindow:
    def test_alerts_pops(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(base_url)
        parentHandle = driver.current_window_handle
        print(parentHandle)

        driver.find_element(By.ID, "openwindow").click()
        time.sleep(4)

        handles = driver.window_handles
        for handle in handles:
            print(handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("Python")
                time.sleep(5)
                driver.close()
                break

        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID,"name").send_keys("Test Successful", Keys.RETURN)
        time.sleep(4)






obj = SwitchWindow()
obj.test_alerts_pops()
