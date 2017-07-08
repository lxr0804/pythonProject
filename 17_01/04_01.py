# coding=utf-8
from time import time

t = time()
if t % 60 == 0:
    print "On the hour"
else:
    print "not on the hour"
