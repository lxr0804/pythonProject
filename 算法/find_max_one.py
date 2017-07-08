# coding=utf-8
a1 = [1, 1, 1, 0, 0]
a2 = [1, 1, 1, 1, 0]
a = [a1, a2]

for i in a:
    for j in i:
        print j
    print "---"

# 当前1最多的行的下标
max_index = 0

# 1最多的行
max_line = 0

# 记录行号
line = 0
for i in a:
    # 行号加1
    line += 1
    # 记录当前数组j中1的个数
    index = 0
    for j in i:
        if j == 1:
            index += 1
        else:
            if index > max_index:
                max_index = index
                max_index = line
            break

print line - 1
