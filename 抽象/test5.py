def story(**kwds):
    return "long long ago, there is a %(job)s called %(name)s " % kwds


print story(name='wbb', job='king')

print pow(2, 3)
print (5,) * 2

x = 1


def change_global():
    global x
    x += 1


change_global()
print x
