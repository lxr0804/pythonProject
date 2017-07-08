# coding=utf-8
# %r用rper()方法处理对象

# %s用str()方法处理对象

print "I'm %r years old" % 22
print "I'm %s years old" % 22

text = "I'm %r years old" % 22
print 'I said %r' % text
print 'I said %s' % text

# %r打印时能够重现它所代表的对象(rper() unambiguously recreate the object it represents)

import datetime
d = datetime.date.today()
print '%r' % d
print '%s' % d
