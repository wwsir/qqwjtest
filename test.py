from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
import json,

listCookies = []
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
    print(listCookies)

for cookie in listCookies:
    print('name is: %s, value is: %s'%(cookie['name'],cookie['value']))

#driver.quit()