#!/usr/bin/python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# import importlib
# importlib.reload(sys)
import pytest
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.touch_actions import TouchActions
from Base.Base import Base
from Base.Huadong import Huadong
import Page
import time

class Person_info(Base,Huadong):
    def __init__(self,driver):
        Base.__init__(self,driver)
        Huadong.__init__(self,driver)
        self.driver = driver
    def check_page_info(self):
        assert self.find_element_x(Page.pers_return),'cant find return button'
        assert self.find_element_x(Page.pers_name), 'cant find user name'
        assert self.find_element_x(Page.pers_share), 'cant find share button'
        assert self.find_element_x(Page.pers_fans), 'cant find fans data'
        assert self.find_element_x(Page.pers_subscribe), 'cant find my subscribe users'
        assert self.find_element_x(Page.pers_exam), 'cant find exam button'
        assert self.find_element_x(Page.pers_modify_info), 'cant find modify button'
        assert self.find_element_x(Page.pers_game), 'cant find game text'
        assert self.find_element_x(Page.pers_note), 'cant find note text'
        assert self.find_element_x(Page.pers_setting), 'cant find setting button'
        assert self.find_element_x(Page.pers_pay), 'cant find pay button'
        assert self.find_element_x(Page.pers_exchange), 'cant find exchange button'
        assert self.find_element_x(Page.pers_evalution),'cant find evalution button'
        assert self.find_element_x(Page.pers_played), 'cant find played button'
        assert self.find_element_x(Page.pers_purchased), 'cant find purchase button'
        assert self.find_element_x(Page.pers_favorites), 'cant find favorites button'
        print('person_page info is complete')
        time.sleep(5)
    def exam_share(self):
        self.click_element(Page.pers_exam)
        assert self.find_element_x(Page.exam_title),'page error'
        self.click_element(Page.exam_confirm)
        assert self.find_element_x(Page.exam_start),'page error'
        self.click_element(Page.exam_share)
        time.sleep(1)
        self.click_element(Page.share_more)
        time.sleep(1)
        self.driver.keyevent(4)
        time.sleep(1)
        self.click_element(Page.exam_share)
        self.click_element(Page.share_weixin)
        time.sleep(2)
        self.click_element(Page.wx_return)
        time.sleep(2)

        self.click_element(Page.exam_share)
        self.click_element(Page.share_weixin)
        time.sleep(2)
        self.input_element(Page.share_wx_count,Page.wx_count)
        self.input_element(Page.share_wx_pwd,Page.wx_pwd)
        self.click_element(Page.share_wx_confrim)
        # self.driver.keyevent(4)
        self.click_element(Page.wx_tips)
        self.click_element(Page.wx_return)
        time.sleep(5)
    def exam_answer(self):
        #开始答题
        try:
            self.click_element(Page.pers_exam)
            self.click_element(Page.exam_confirm)
            time.sleep(10)
            self.click_element(Page.exam_start)
            self.driver.get_screenshot_as_file('./Screenshots/exam/start_exam.png')
            self.click_element(Page.answer_next)
            self.driver.get_screenshot_as_file('./Screenshots/exam/exam_tips.png')
            # 找不到控件
            # self.click_element(Page.answer_tips)
            #click_position参数写死，会根据屏幕自适配
            self.click_position(535,1048)
            eles = self.find_elements_x(Page.answer_opt)
            for i in range(len(eles)):
                cont = eles[i].get_attribute("name")
                print(eles[i],cont)
                if 'D' in cont:
                    eles[i].click()
                    time.sleep(1)
                    break
            self.click_element(Page.answer_pre)
            time.sleep(1)
            self.click_element(Page.answer_next)
            for i in range(18):
                ele = self.find_elements_x(Page.answer_opt)
                for j in range(len(ele)):
                    cont = ele[j].get_attribute("name")
                    print(ele[j], cont)
                    if 'D' in cont:
                        ele[j].click()
                        time.sleep(1)
                        break

            time.sleep(5)
            self.driver.get_screenshot_as_file('./Screenshots/exam/answer.png')
            self.click_position(329,1344)
            time.sleep(5)
        except Exception as e:
            print(e)

        # 修改资料
    def modify_person_data(self):
        self.click_element(Page.pers_modify_info)
        time.sleep(2)
        self.driver.get_screenshot_as_file('./Screenshots/modify_data/modify_01.png')
        nick_name = 'yuanyuan'
        nick = self.find_element_x(Page.edit_nickname)
        nick.clear()
        self.input_element(Page.edit_nickname, nick_name)
        self.click_element(Page.edit_birthday)
        time.sleep(1)
        self.click_element(Page.brithday_cancel)
        """
        无法获得数字，只能根据当前时间和目标时间来选择滑动步数
        """
        self.click_element(Page.edit_birthday)
        time.sleep(1)
        #获得当前时间，分离出年月日
        t = self.time_split()
        year = int(t[0])
        mon = int(t[1])
        day = int(t[2])
        self.time_swipe(2010,1,12,year,mon,day)
        time.sleep(1)
        self.click_element(Page.brithday_confirm)
        # 选择性别
        self.click_element(Page.edit_gender)
        self.click_element(Page.gender_female)
        self.click_element(Page.edit_country)
        time.sleep(1)
        self.click_element(Page.country_afh)
        data = 'this is a profile'
        self.huadong_up()
        time.sleep(1)
        self.input_element(Page.edit_profile, data)
        self.driver.get_screenshot_as_file('./Screenshots/modify_data/edit_info.png')
        time.sleep(1)
        self.click_element(Page.edit_save)
        # assert self.find_element_x(Page.edit_tips),'save error'
        time.sleep(5)
        self.click_element(Page.edit_country)
        for i in range(100):
            eles = self.find_elements_x(Page.country)
            x = []
            for i in eles:
                x.append(i.text)
            if '中国' in x:
                self.click_element(Page.country_china)
                break
            self.huadong_up()
            time.sleep(1)
        time.sleep(2)
        self.click_element(Page.edit_save)
        time.sleep(2)









