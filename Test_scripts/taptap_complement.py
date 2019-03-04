#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from Base.Base import Base
import Page
from Page.login import Login
import pytest
import time
import importlib
import sys
importlib.reload(sys)

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

    def teardown_class(self):
        if self.driver:
            self.driver.quit()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>teardown")
    def tap_test(self):
        update = self.driver.find_element(By.ID,'com.taptap:id/btn_update')
        assert update, 'no update'
        self.driver.get_screenshot_as_file("./Screenshots/login/update_window.png")
        self.driver.find_element(By.ID,'com.taptap:id/btn_cancel').click()
        self.driver.get_screenshot_as_file("./Screenshots/login/main_scene.png")
        time.sleep(2)
        self.driver.click_element(Page.leaderboard)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_leaderboard.png")
        self.driver.click_element(Page.plaza)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_plaza.png")
        self.driver.click_element(Page.my_interest)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_community.png")
        self.driver.click_element(Page.my_games)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_games.png")
        self.driver.click_element(Page.game_recom)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_market.png")
        self.driver.click_element(Page.go_to_setting)
        time.sleep(2)
