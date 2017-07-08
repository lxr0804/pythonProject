# coding=utf-8
# 参数前面加上*就是可变参数,传入的参数数量不限,如下给定a,b,c...计算a2+b2+...
def cal(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    print sum


n = [1, 2, 3, 4, 4]
cal(*n)
