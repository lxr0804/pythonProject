# coding=utf-8

x = ['qw', 'lius', 'sdsda', 's', 'sf']
# 按照长度排序
x.sort(key=len)
print x

y = [1, 2, 24, 45, 562, 3, 45, 24]
# 倒叙排列,reverse默认false为正序
y.sort(reverse=True)
print y

print sorted(y)

# 把列表转化成元组
y = tuple(x)
print y

seq = [3, 2, 1, 4, 5]
seq.sort()
print seq
