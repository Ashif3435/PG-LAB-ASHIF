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