def hello(a, b):
    print "%s, %s" % (a, b)


def hello2(a='hello', b='world'):
    print "%s, %s" % (a, b)


hello('mmm', 'nnn')

hello(a='hello', b='liuxr')
hello2()
hello2(b='liuxr')
