from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import time


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.baseURL = "https://magento.com/products/open-source"
        self.driver.get(self.baseURL)

    def test_register_new_user(self):
        driver = self.driver

        driver.find_element(By.LINK_TEXT, "MY ACCOUNT").click()
        registerbtn = driver.find_element(By.XPATH, "//span[text()='Register']")
        self.assertTrue(registerbtn.is_displayed() and registerbtn.is_enabled())

        registerbtn.click()
        self.assertEqual("Create New Customer Account", driver.title)

        # get all the elements from Register page

        first_name = driver.find_element(By.ID, "firstname")
        last_name = driver.find_element(By.ID, "lastname")
        email_address = driver.find_element(By.ID, "email_address")
        company = driver.find_element(By.ID, "customer_company_type")
        sel_company = Select(company)
        sel_company.select_by_index(4)

        customer = Select(driver.find_element(By.ID, "customer_individual_role"))
        for options in customer.options:
            print(options.text, options.get_attribute('value'))

        customer.select_by_index(2)

        # customer = driver.find_element(By.ID, "customer_individual_role")
        # sel_customer = Select(customer)
        # sel_customer.select_by_index(2)
        screen_name = driver.find_element(By.ID, "screen_name")
        password = driver.find_element(By.ID, "password")
        confirm_password = driver.find_element(By.ID, "confirmation")
        agree_terms = driver.find_element(By.XPATH, "//input[@type='checkbox'][@id='agree_terms']")
        submit = driver.find_element(By.XPATH, "//button[@title='Submit']")

        # self.assertEqual(255, int(first_name.get_attribute("maxlength")))

        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled()
                        and company.is_enabled() and screen_name.is_enabled()
                        and password.is_enabled() and confirm_password.is_enabled() and agree_terms.is_enabled()
                        and submit.is_enabled())

        # check agreement terms is unchecked
        self.assertFalse(agree_terms.is_selected())
        user_name = "user_" + strftime("%H%M%S", gmtime())
        first_name.send_keys("Test1")
        last_name.send_keys(user_name)
        email_address.send_keys(user_name + "@example.com")
        screen_name.send_keys(user_name)
        password.send_keys("1Tester@")
        confirm_password.send_keys("1Tester@")
        agree_terms.click()

        submit.click()

        time.sleep(15)
        self.takeScreenshot(driver)
        print(self.takeScreenshot)

    def takeScreenshot(self, driver1):
        """
        take screenshor of the current open browser window
        :param driver1:
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        scrnshotdir = "C:\\Users\\qa247\\Desktop\\"
        destinationFile = scrnshotdir + fileName


        try:
            driver1.save_screenshot(destinationFile)
            print("Screenshot saved to directory" + destinationFile)
        except NotADirectoryError:
            print("Not a valid directory")



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


