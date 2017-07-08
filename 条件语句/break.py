from math import sqrt
for x in range(99, 0):
    y = sqrt(x)
    if y == int(y):
        print x
        break