from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RunChromeTest1:

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:\\Builds\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        # practice_page = driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        # driver.implicitly_wait(30)

        elementByTagName = driver.find_elements_by_tag_name("a")
        driver.implicitly_wait(30)

        for i in elementByTagName:
            print(i.text)





# RunChromeTest1.test("run")

runtest = RunChromeTest1()
runtest.test()


