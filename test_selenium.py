#coding=utf-8

from selenium import webdriver
from time import sleep
import json,pickle,sys,traceback

driver = webdriver.Firefox(r"E:\43j6ugol.d")
driver.get("https://wj.qq.com/")

#store cookie for future use
# sleep(40)
# pickle.dump( driver.get_cookies(), open("cookies.pkl","wb"))

#close dialog
try:
    driver.find_element_by_class_name("ui-dialog-close")
    dialog = driver.find_element_by_class_name("ui-dialog-close")
    dialog.click()
except:
 print('dialog not found.')

#maxmize Browser
driver.maximize_window()

#write cookie to aumated login
try:
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        #print(cookie)
        new_cookie = {}
        new_cookie['name'] = cookie['name']
        new_cookie['value'] = cookie['value']
        driver.add_cookie(new_cookie)
except:
    traceback.print_exc()
driver.refresh()

if driver.find_element_by_id('logout').text=='退出':
    print('Login succeed')
else:
    print('Login failed')

#scroll up and down
def scroll_up_down(number = 2):
    for i in range(0,number):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)
        driver.execute_script("window.scrollTo(0,0)")
        sleep(1)
        print("scroll up and down %s" %(i))

driver.find_element_by_id("get_started_btn").click()
sleep(10)
driver.find_element_by_css_selector('[href="/edit.html?tid=36"]').click()
sleep(10)
driver.find_element_by_css_selector('[id="publish_survey"]').click()
sleep(5)
driver.find_element_by_css_selector('[i-id="保存"]').click()

#scroll_up_down(number=3)

# driver.quit()
