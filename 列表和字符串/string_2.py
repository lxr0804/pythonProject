
from string import Template
from math import pi

s = Template('hello,$x')
print s.substitute(x='world')
y = Template('I have 3$$ , $a')
print y.substitute(a='haha')
print '%s plus %s equals'

print '%i' % pi

