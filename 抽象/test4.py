def test(*a):
    print a


def test2(**a):
    print a


def test3(x, y, z=3, *a, **b):
    print x, y, z
    print a
    print b


test('b')
test2(x=1)
test3(1, 2, 3, 4, 5, 67, 8, 'lll', m='lxr', n='wbb')
