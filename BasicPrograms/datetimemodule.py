import datetime
import time
# print(time.time())
# print((time.asctime()))
# chaitanya=datetime.datetime.now()
# print(chaitanya)
# print("year:",chaitanya.year)
# print("month:",chaitanya.month)
# print("day:",chaitanya.day)
# print("hour:",chaitanya.hour)
# print("minute:",chaitanya.minute)
# print("second:",chaitanya.second)
# import calendar
# s=calendar.prcal(3023)
# s2=calendar.month(2024,2)
# print(s2)
# s1=calendar.isleap(2005)
# print(s1)
# import datetime
# x=datetime.datetime.now()
# print(x)
# from datetime import timedelta
# print(x+timedelta(days=-89))
import time
from datetime import datetime
import pytz
time1=pytz.timezone('Japan')
print("CURRENT TIME IS:",datetime.now(time1))