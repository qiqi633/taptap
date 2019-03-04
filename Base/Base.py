#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions
# import importlib
# import sys
# importlib.reload(sys)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time
import pytest

class Base:
    def __init__(self,driver):
        self.driver = driver
    def find_element_x(self,loc,timeout = 20,poll = 1):
        """
        :param loc: 键值对，元素定位方式，和元素值（By.ID,'VALUE'）
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
        # return self.driver.find_element(*loc)
    def click_element(self,loc):
        self.find_element_x(loc).click()
    def input_element(self,loc,text):
        self.find_element_x(loc).send_keys(text)
    def long_press_element(self,loc):
        button = self.find_element_x(loc)
        TouchActions(self.driver).long_press(button,2000).release().perform()

    def find_elements_x(self,loc,timeout=20,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    def click_position(self,x,y):
        """
        算出点击点 在不同设备的屏幕坐标相对位置
        :param x: 编写脚本时使用设备的横坐标
        :param y: 编写脚本时使用设备的纵坐标
        :return:
        """
        pix = self.driver.get_window_size()
        #x,y坐标在屏幕的位置系数，计算出原设备上， 定位点的相对位置,华为荣耀6X，分辨率{'width': 1080, 'height': 1812}

        x_perc = float(x)/1080
        y_perc = float(y)/1812
        x_new = x_perc*pix['width']
        y_new = y_perc*pix['height']
        print("pix:{0},x_new:{1},y_new:{2},x_perc:{3},y_perc:{4},x:{5},y:{6}".format(pix,x_new,y_new,x_perc,y_perc,x,y))
        self.driver.tap([(x_new,y_new)],500)
    def time_split(self):
        loctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(loctime)
        tim = re.split('-| |:', loctime)
        return tim






