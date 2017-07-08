def x(m):
    def y(n):
        return m * n

    return y


a = x(2)
print a(5)

r = 5
for i in range(1, r):
    r = r * i

print r