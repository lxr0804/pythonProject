# coding=utf-8
lst= {1, 2, 3, 231, 234, 2312}
print max(lst)
print min(lst)
print len(lst)

print ''.join(['e', 's'])

number = [1, 4, 6, 7, 7, 7]

number[1:1] = [2, 3]
print number
del number[1]
print number
number[1:2] = []
print number
# 追加单个值
number.append(5)
# 追加多个值
number.extend([8,9])
print number
# 排序
print sorted(number)
# 输出7的个数
print number.count(7)
# 4的位置
print number.index(4)
# 插入一个元素'liuxr'
number[2:2] = ['liuxr']
print number
number.insert(3, 'wangbb')
print number
# 移除一个元素
number.pop(0)
print number
# 反向存放
number.reverse()
print number
# 比较大小,大于返回1,小于返回-1,等于返回0
print cmp(10, 20)
print cmp(10, 10)
print cmp(20, 10)

