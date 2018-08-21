from selenium import webdriver
from selenium.webdriver.common.by import By
import http.client


baseURL1 = "https://www.msn.com"
driver =webdriver.Chrome(r"C:\Builds\chromedriver.exe")
driver.get(baseURL1)
driver.maximize_window()
driver.implicitly_wait(30)

elements = driver.find_elements(By.TAG_NAME, "a")
print(len(elements))

# To find broken links
conn = http.client.HTTPSConnection("www.msn.com")
conn.request("GET", "/")
r1 = conn.getresponse()
for element in elements:
    if r1.status == 404:
        print(element.get_attribute("href"))
        print(r1.status, r1.reason)




driver.quit()

