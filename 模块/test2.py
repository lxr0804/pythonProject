# coding=utf-8
import time
import datetime

print time.ctime()

now_time = datetime.datetime.now()

print now_time
# 当前时间前一天
yesterday = now_time + datetime.timedelta(days=-1)
print yesterday
# 当前时间的前一分钟
now_old = now_time + datetime.timedelta(minutes=-1)
print now_old
