def checkOnce2(l):
    d = dict()
    for i in l:
        d[i] = d.get(i, 0) + 1

    ls = []
    for (k, v) in d.items():
        if v == 1:
            ls.append(k)

    return ls


print checkOnce2([1, 2, 3, 2, 2])

zd = dict()
zd[1] = zd.get + 1
print zd[1]
