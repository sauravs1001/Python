# from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
import  csv

driver = webdriver.Chrome(r"C:\Builds\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://econpy.pythonanywhere.com/ex/001.html")

buyers = driver.find_elements_by_xpath("//div[@title = 'buyer-name']")
prices = driver.find_elements_by_xpath("//span[@class = 'item-price']")

for i in range(len(buyers)):
    print(buyers[i].text + " : " + prices[i].text)

driver.close()



# CODES FROM WEB SCRAPING USING BEATIFUL SOUP MODULE
# res = requests.get("http://quotes.toscrape.com/")
# # print(res.text)
# soup = BeautifulSoup(res.text, 'lxml')
# print(soup)