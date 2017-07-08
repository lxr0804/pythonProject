# coding=utf-8
# break 结束整个循环
for letter in "hello":
    if letter == 'l':
        break
    print 'The current letter is', letter

var = 10
while var > 3:
    print 'The var is ', var
    var -= 1
    if var == 6:
        break
print "bye"

