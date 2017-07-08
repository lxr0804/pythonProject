# coding=utf-8
# continue 结束本次循环,剩下的会继续执行

for letter in 'hello':
    if letter == 'l':
        continue
    print 'The letter is', letter


var = 10
while var > 3:
    print 'The var is ', var
    var -= 1
    if var == 6:
        continue
print "bye"
