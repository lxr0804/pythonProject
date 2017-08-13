def reverseWords(s):
    l = len(s)
    if l == 1:
        return s[0]
    if l == 0:
        return -1
    listS = s.strip().split(' ')
    res = []
    for i in listS[::-1]:
        res.append(i)
    return ' '.join(res)


print reverseWords('hello')
print reverseWords(' ')
print (' hello world ')
x = []
