# Dynamic Xpath Example

# Using contains keyword
# //div[contains(@class, 'course-listing-title') and contains(text(), 'JavaScript for beginners')]

from selenium import webdriver
from selenium.webdriver.common.by import By

class DynamicXpathUtility:
    def test_dynamic_xpath(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseURL)

        # Login to the Course page
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for Courses
        searchBox =driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")
        driver.find_element(By.ID, "search-course-button").click()

        # Select Courses
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


chrmobj = DynamicXpathUtility()
chrmobj.test_dynamic_xpath()
