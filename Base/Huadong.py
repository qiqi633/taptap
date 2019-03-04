#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions
import Base
from Base import Base
import pytest
# import importlib
# import sys
# importlib.reload(sys)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Huadong:
    def __init__(self,driver):
        self.driver = driver
    def huadong_up(self):
        pix = self.driver.get_window_size()
        start_x = pix['width' ] *0.5
        start_y = pix['height' ] *0.8
        end_x = pix['width'] * 0.5
        end_y = pix['height'] * 0.5
        self.driver.swipe(start_x ,start_y ,end_x ,end_y ,2000)
    def huadong_down(self):
        pix = self.driver.get_window_size()
        start_x = pix['width'] * 0.5
        start_y = pix['height'] * 0.8
        end_x = pix['width'] * 0.5
        end_y = pix['height'] * 0.5
        self.driver.swipe(end_x, end_y, start_x, start_y, 2000)
    def huadong_turnright(self):
        pix = self.driver.get_window_size()
        start_x = pix['width'] * 0.6
        start_y = pix['height'] * 0.5
        end_x = pix['width'] * 0.3
        end_y = pix['height'] * 0.5
        self.driver.swipe(end_x, end_y, start_x, start_y, 2000)
    def huadong_turnleft(self):
        pix = self.driver.get_window_size()
        start_x = pix['width'] * 0.6
        start_y = pix['height'] * 0.5
        end_x = pix['width'] * 0.3
        end_y = pix['height'] * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
    def huadong_position(self,start_x,start_y,end_x,end_y):
        """
        指定滑动位置，根据屏幕大小自适应，入参写死 ，写脚本手机屏幕是（1080，1812）
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :return:
        """
        pix = self.driver.get_window_size()
        start_x_perc = float(start_x)/1080
        start_y_perc = float(start_y)/1812
        end_x_perc = float(end_x)/1080
        end_y_perc = float(end_y)/1812
        self.driver.swipe(start_x_perc*pix['width'] ,start_y_perc*pix['height'] ,end_x_perc*pix['width'] ,end_y_perc*pix['height'] ,1000)

    # 时间控件，滑动到指定日期
    def time_swipe(self, y, m, d, year, mon,da):
        """

        :param y: 指定年份
        :param m: 指定月份
        :param d: 指定天数
        :param year: 控件当前年份
        :param mon: 控件当前月份
        :param da: 控件当前天数
        :return:
        """
        year_up = (280, 849, 280, 675)
        year_down = (280, 849, 280, 1034)
        mon_up = (550, 849, 550, 675)
        mon_down = (550, 849, 550, 1034)
        day_up = (800, 849, 800, 675)
        day_down = (800, 849, 800, 1034)
        li = [(y, year,year_up,year_down), (m, mon,mon_up,mon_down), (d, da,day_up,day_down)]

        # @pytest.mark.parametrize('t,t_c,t_pu,t_pd', li)
        # parametrize标记的函数怎么才能被调用
        def ymd_huadong(t, t_c, t_pu, t_pd):
            print(t,t_c,t_pd,t_pu)
            if t > t_c:
                for i in range(t - t_c):
                    print(t-t_c)
                    self.huadong_position(*t_pu)
            if t == t_c:
                pass
            if t < t_c:
                for i in range(t_c - t):
                    print(t_c-t)
                    self.huadong_position(*t_pd)

        ymd_huadong(*li[0])
        ymd_huadong(*li[1])
        ymd_huadong(*li[2])



