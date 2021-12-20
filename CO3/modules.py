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
print("....................")
#time
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
print("...................")
#calender module
print("...................")
import calendar
#mm=int(input("enter month:"))
#yy=int(input("enter year:"))
#print(calendar.month(yy,mm))
print("...................")
print(calendar.calendar(2000))
print("...................")
#datetime module
print("..................")
import datetime
t=datetime.time(22,56,44)
print(t)
print("..............")
print("hour",t.hour)
print("minute",t.minute)
print("second",t.second)
print("micro sec",t.microsecond)
print("..................")
d=datetime.date.today()
print(d)
print("yr",d.year)
print("mnth",d.month)
print("day",d.day)
print("...............")
d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=2)
print(td)
d2=d1+td
print(d2)
print("..............")
print()
dt=datetime.datetime.combine(d,t)
print(dt)
print("...................")
#statistic module
import statistics
l=[1,2,3,4,3,5]
print("mean:",statistics.mean(l))
print("median:",statistics.median(l))
print("mode:",statistics.mode(l))
print("harmonic mean:",statistics.harmonic_mean(l))
print("std dev:",statistics.stdev)
print(".................")
#rondom module
print(".............")
import random
l1=["apple","bnanana","orange"]
print("sample",random.sample(l1,k=2))
print("choice",random.choice(l1))
print("choices:",random.choices(l1,k=2))
random.shuffle(l1)