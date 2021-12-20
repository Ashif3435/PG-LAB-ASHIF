#math module
import math
print("the value pie is",math.pi)
print("....................")
import math as m
print("the value of pi is",m.pi)
print("....................")
from math import pi,sqrt
print("value of pi",pi)
print("value squre root of 4",sqrt(4))
print("....................")
print(math.cos(90))
print(math.sin(9))
print(math.tan(0))
#time and calender module
print("....................")
import time
print("current time in sec",time.time())
print("....................")
print("current time:",time.ctime())
print("....................")
print("current time after 30 sec:",time.ctime(time.time()+30))
print("....................")
t=time.localtime()
print("time:",t)
print("....................")
print("current year:",t.tm_year)
print("current month:",t.tm_mon)
print("current day:",t.tm_mday)
print("current hour:",t.tm_hour)
print("current min:",t.tm_min)
print("current sec:",t.tm_sec)
print("current weakday:",t.tm_wday)