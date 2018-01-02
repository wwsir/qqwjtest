#防止中文乱码
#coding=utf-8
from selenium import webdriver

#加载unittest模块
import unittest
import time


class BaiduYun(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.base_url="https://www.baidu.com"
        self.verficationErrors=[]
        self.accept_next_alert=True

    def test_Register(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        u"""立即注册百度账号"""
        browser.find_element_by_class_name("lb").click()
        time.sleep(2)
        browser.find_element_by_css_selector("[title='用户名登录'']").click()
        browser.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("13485069690")


    def tearDown(self):
        self.browser.quit()
        self.assertEqual([],self.verficationErrors)
if __name__=="__main__":
    unittest.main()
