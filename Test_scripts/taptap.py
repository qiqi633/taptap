#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from Base.Base import Base
import Page
from Page.login import Login
from Page.person_info import Person_info
import pytest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# import importlib
# import sys
# importlib.reload(sys)

class Taptap:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'S9B7N17819001588'
        desired_caps['appPackage'] = 'com.taptap'
        desired_caps['appActivity'] = 'com.play.taptap.ui.MainAct'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>setup")
        self.tap = Login(self.driver)
        self.per = Person_info(self.driver)

    def teardown_class(self):
        if self.driver:
            self.driver.quit()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>teardown")
    def tap_test(self):
        self.tap.goto_main()
        # self.tap.main_page()
        self.tap.goto_persion_page()
        # self.tap.register_failture()
        # self.tap.login_failture()
        # data = '密码安全'
        # class_n = 'android.widget.TextView'
        # ele_s = (By.XPATH,"//*[contains(@text,'密码安全')]")
        # self.tap.get_ele_up(class_n,data,ele_s)
        # self.tap.change_pwd()
        # self.per.check_page_info()
        # self.per.exam_share()

        # self.per.exam_answer()
        self.per.modify_person_data()

