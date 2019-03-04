#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Base.Base import Base
from Base.Huadong import Huadong
import Page
import sys
import time
from selenium.webdriver.common.touch_actions import TouchActions
# import importlib
# import sys
# importlib.reload(sys)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pytest



class Login:
    def __init__(self,driver):
        self.obj = Base(driver)
        self.hua = Huadong(driver)
        self.driver =driver
    def goto_main(self):
        update = self.obj.find_element_x(Page.app_update)
        assert update,'no update'
        self.driver.get_screenshot_as_file("./Screenshots/login/update_window.png")
        self.obj.click_element(Page.app_update_cancel)
        self.driver.get_screenshot_as_file("./Screenshots/login/main_scene.png")
        time.sleep(2)
    def main_page(self):
        self.obj.click_element(Page.leaderboard)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_leaderboard.png")
        self.obj.click_element(Page.plaza)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_plaza.png")
        self.obj.click_element(Page.my_interest)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_community.png")
        self.obj.click_element(Page.my_games)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_games.png")
        self.obj.click_element(Page.game_recom)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_market.png")
    def goto_persion_page(self):
        self.obj.click_element(Page.go_to_setting)
        time.sleep(2)
    def register_failture(self):

        assert self.obj.find_element_x(Page.login_has_account),'goto setting page failed'
        time.sleep(2)
        #注册用例
        #空号码点击注册
        self.obj.click_element(Page.login_regis)

        #输入号码注册
        assert self.obj.find_element_x(Page.login_cellnum), 'cant find input text'
        self.obj.input_element(Page.login_cellnum,Page.login_data)
        time.sleep(5)
        self.driver.get_screenshot_as_file("./Screenshots/login/login_cellnum.png")
        self.obj.click_element(Page.login_regis)

        #输入验证码界面，不输入直接关闭，输入错误的关闭
        self.obj.click_element(Page.login_verfi_close)
        self.obj.click_element(Page.login_regis)
        self.obj.input_element(Page.login_verfi_text,Page.verfi_code)
        assert self.obj.find_element_x(Page.verfi_error),'verify error'
        self.driver.get_screenshot_as_file('./Screenshots/login/verfiy_error')
        self.obj.click_element(Page.login_verfi_close)
        time.sleep(5)

    def login_failture(self):
        #切换登录方式页签，使用邮箱登录
        self.obj.click_element(Page.login_has_account)
        self.driver.get_screenshot_as_file('./Screenshots/login/login_page')
        self.obj.click_element(Page.login_account_email)
        time.sleep(2)
        self.obj.click_element(Page.login_account_cellnum)

        self.obj.click_element(Page.account_ver)

        self.obj.input_element(Page.account_cellnum,Page.account_num)
        self.driver.get_screenshot_as_file('./Screenshots/login/phonenumber_login')
        self.obj.click_element(Page.account_ver)
        self.obj.input_element(Page.account_ver_code,Page.verfi_code)
        assert self.obj.find_element_x(Page.verfi_error),'verify error'
        # #重新发送验证码,点击重新发送按钮失败，为啥
        # cc = self.obj.find_element_x(Page.account_ver_code)
        # cc.clear()
        # self.obj.click_element(Page.veri_resend)
        # print("checkpoint:send message again")
        # assert self.obj.find_element_x(Page.verfi_code1).text is None,'resend verify code error'
        self.obj.click_element(Page.login_verfi_close)
        time.sleep(2)



    #修改密码
    @pytest.fixture()
    def get_need_element_up(self):
        """

        :param ele_name: class_name
        :param need_element: 待查找的text
        :return:
        """
        i = 20
        while i>=0:
            print(i)
            ele = self.driver.find_elements_by_class_name('android.widget.TextView')
            print(ele)
            for e in ele:
                print(e)
                if e.text == '密码安全':
                    e.click()
                    return
            self.hua.huadong_up()
            i-=1

    @pytest.mark.usefixtures("get_need_element_down")
    def get_ele_up(self,class_na,data,ee):
        """
        此方法只适用于以elements_class_name查找方式，
        :param class_na: class 元素组名字
        :param data: 待查找的按钮文本
        :param ee: 待查找的按钮元素
        :return:
        """
        self.obj.click_element(Page.per__set)
        assert self.driver.find_element_by_xpath("//*[contains(@text,'新版本设置')]"),'into setting successfuly'
        for n in range(20):
            print(n)
            eles = self.driver.find_elements_by_class_name(class_na)
            print(eles)
            el = []
            for e in eles:
                el.append(e.text)
            print(el)
            if data in el:
                self.obj.click_element(ee)
                break
            else:
                self.hua.huadong_up()
                time.sleep(2)
        time.sleep(2)
    def change_pwd(self):
        self.obj.input_element(Page.input_pwd_old,Page.pwd_old)
        self.obj.input_element(Page.input_pwd_new,Page.pwd_new)
        self.obj.input_element(Page.input_pwd__new_again,Page.pwd_new)
        self.obj.click_element(Page.pwd_eye)
        self.driver.get_screenshot_as_file('./Screenshots/login/set_pwd.png')
        self.obj.click_element(Page.check_button)
        time.sleep(5)












