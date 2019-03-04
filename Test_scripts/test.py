import time
import re
import pytest
import Test_scripts
loctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(loctime)
time = re.split('-| |:',loctime)
print(time,time[0],type(int(time[0])))

year = int(time[0])
mon = int(time[1])
da = int(time[2])
y =1977
m=1
d=22
list=[(y,year,Test_scripts.year_up,Test_scripts.year_down),(m,mon,Test_scripts.mon_up,Test_scripts.mon_down),(d,da,Test_scripts.day_up,Test_scripts.day_down)]
def test(x1,x2,x3,x4):
    print(x1,x2,x3,x4)

@pytest.mark.parametrize('t,t_c,up,down',list)
def ymd(t,t_c,up,down):
    print("t,t_c,up,down:",t,t_c,up,down)
    if t > t_c:
        for i in range(t-t_c):
            print(t,t_c,i)
            test(*up)
    if t == t_c:
        pass
    if t < t_c:
        for i in range(t_c-t):
            print(t,t_c,i)
            test(*down)
ymd(*list[0])
ymd(*list[1])
ymd(*list[2])