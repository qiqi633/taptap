#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
# import importlib
# import sys
# importlib.reload(sys)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#login elements
app_update = (By.ID,'com.taptap:id/btn_update')
app_update_cancel = (By.ID,'com.taptap:id/btn_cancel')

go_to_setting = (By.ID,'com.taptap:id/head_portrait')
login_cellnum = (By.XPATH,"//*[contains(@text,'请输入手机号码')]")
login_regis =(By.ID,'com.taptap:id/login_register_btn')
login_data = '18603060289'
login_has_account = (By.XPATH,"//*[contains(@text,'有帐号?去登录')]")



#主界面元素：
game_recom = (By.ID,'com.taptap:id/game_market')
leaderboard = (By.ID,'com.taptap:id/rank')
plaza = (By.ID,'com.taptap:id/classify')
my_interest = (By.ID,'com.taptap:id/community')
my_games = (By.ID,'com.taptap:id/my_game')

login_account_cellnum = (By.ID,'com.taptap:id/login_phone')
login_account_email = (By.ID,'com.taptap:id/login_mail')
account_cellnum = (By.XPATH,"//*[contains(@text,'请输入手机号码')]")
account_email = (By.XPATH,"//*[contains(@text,'请输入邮箱地址')]")
email_pwd =(By.XPATH,"//*[contains(@text,'请输入登录密码')]")
account_num = '13590356619'
account_ver =(By.ID,'com.taptap:id/login_register_btn')
account_ver_code = (By.ID,'com.taptap:id/item_edittext')
veri_resend = (By.ID,'com.taptap:id/send_again')

verfi_code = '123456'
verfi_error = (By.XPATH,"//*[contains(@text,'验证码错误')]")
verfi_code1 = (By.ID,'com.taptap:id/item_code_iv1')
verfi_code2 = (By.ID,'com.taptap:id/item_code_iv2')
verfi_code3 = (By.ID,'com.taptap:id/item_code_iv3')
verfi_code4 = (By.ID,'com.taptap:id/item_code_iv4')
verfi_code5 = (By.ID,'com.taptap:id/item_code_iv5')
verfi_code6 = (By.ID,'com.taptap:id/item_code_iv6')

login_verfi_close = (By.ID,'com.taptap:id/close')
login_verfi_text = (By.ID,'com.taptap:id/item_edittext')

#已登录设置中心元素
per__set = (By.ID,'com.taptap:id/taper_setting')
set_class = 'android.widget.TextView'
pwd_scr = (By.XPATH,"//*[contains(@text,'密码安全')]")

#设置密码
input_email = (By.XPATH,"//*[contains(@text,'输入邮箱')]")
input_pwd = (By.XPATH,"//*[contains(@text,'输入密码')]")
input_pwd_again = (By.XPATH,"//*[contains(@text,'再次输入邮箱')]")
input_pwd_old = (By.XPATH,"//*[contains(@text,'输入旧密码')]")
input_pwd_new = (By.XPATH,"//*[contains(@text,'输入新密码')]")
input_pwd__new_again = (By.XPATH,"//*[contains(@text,'再次输入新密码')]")
check_button = (By.ID,'com.taptap:id/password_btn')
pwd_eye = (By.ID,'com.taptap:id/password_pw_eye')
email = '630345353@qq.com'
pwd_old = '0117151026imok'
pwd_new = '0117151026imok'

#已登录个人信息主界面元素
pers_return = (By.CLASS_NAME,'android.widget.ImageButton')
pers_name = (By.ID,'com.taptap:id/taper_name')
pers_share = (By.ID,'com.taptap:id/taper_share')
pers_fans = (By.XPATH,"//*[contains(@text,'粉丝')]")
pers_subscribe = (By.XPATH,"//*[contains(@text,'关注')]")
pers_sign = (By.ID,'com.taptap:id/taper_about')
pers_exam = (By.ID,'com.taptap:id/taper_etiquette')
pers_modify_info = (By.ID,'com.taptap:id/taper_modify')
pers_game = (By.XPATH,"//*[contains(@text,'游戏')]")
pers_note = (By.XPATH,"//*[contains(@text,'帖子')]")

pers_played = (By.XPATH,"//*[contains(@text,'玩过')]")
pers_purchased = (By.XPATH,"//*[contains(@text,'购买')]")
pers_evalution = (By.XPATH,"//*[contains(@text,'评价')]")
pers_favorites= (By.XPATH,"//*[contains(@text,'收藏')]")

pers_reply = (By.XPATH,"//*[contains(@text,'回帖')]")

pers_setting = (By.ID,'com.taptap:id/taper_setting')
pers_pay = (By.ID,'com.taptap:id/taper_pay')
pers_exchange = (By.ID,'com.taptap:id/taper_pay')


#考试流程使用元素
exam_title = (By.ID,'com.taptap:id/dialog_title')
exam_cont = (By.ID,'com.taptap:id/dialog_content')
exam_intr = (By.XPATH,"//*[contains(@text,'TapTap礼仪考试说明')]")
exam_giveup = (By.ID,'com.taptap:id/dialog_btn_left')
exam_confirm = (By.ID,'com.taptap:id/dialog_btn_right')

exam_start = (By.ID,'test-start')
exam_share = (By.ID,'com.taptap:id/share')
exam_return_txt = (By.ID,'com.taptap:id/back')
exam_return_btn = (By.CLASS_NAME,'android.widget.ImageButton')

share_weixin = (By.XPATH,"//*[contains(@text,'微信')]")
share_qq = (By.XPATH,"//*[contains(@text,'QQ')]")
share_more =(By.XPATH,"//*[contains(@text,'更多')]")

share_wx_count = (By.XPATH,"//*[contains(@text,'请填写微信号/QQ号/邮箱')]")
share_wx_pwd = (By.XPATH,"//*[contains(@text,'请填写密码')]")
wx_count = 'dfdfdsfdf'
wx_pwd = '1234566789'

wx_return = (By.ID,'com.tencent.mm:id/kb')
share_wx_confrim = (By.ID,'com.tencent.mm:id/cov')
wx_tips = (By.XPATH,"//*[contains(@text,'确定')]")



#答题页面
answer_next = (By.ID,'next-question-step2-1')
answer_pre = (By.ID,'prev-question-step2-2')

answer_tips = (By.XPATH,"//*[contains(@text,'确定')]")
answer_opt = (By.CLASS_NAME,'android.view.View')



#编辑资料页面元素
edit_save = (By.ID,'com.taptap:id/save')
edit_return = (By.CLASS_NAME,'android.widget.ImageButton')
edit_nickname = (By.ID,'com.taptap:id/nick_name_input_box')
edit_birthday = (By.ID,'com.taptap:id/birthday')
edit_gender = (By.ID,'com.taptap:id/gender')
edit_country = (By.ID,'com.taptap:id/countries')
edit_num = (By.ID,'com.taptap:id/phone_number_input_box')
edit_profile = (By.ID,'com.taptap:id/personal_profile')
birthday = (By.ID,'android:id/numberpicker_input')
brithday_cancel = (By.ID,'android:id/button2')
brithday_confirm = (By.ID,'android:id/button1')
brithday_year = (By.XPATH,"//*[contains(@text,'1977')]")
brithday_month = (By.XPATH,"//*[contains(@text,'1')]")
brithday_day = (By.XPATH,"//*[contains(@text,'22')]")

gender_male = (By.XPATH,"//*[contains(@text,'男')]")
gender_female = (By.XPATH,"//*[contains(@text,'女')]")
country = (By.CLASS_NAME,'android.widget.TextView')
country_afh = (By.XPATH,"//*[contains(@text,'阿富汗')]")
country_china = (By.XPATH,"//*[contains(@text,'中国')]")

edit_tips = (By.XPATH,"//*[contains(@text,'你设置的国家/地区与所在位置不相符')]")