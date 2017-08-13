d = dict(a='liuxr', b='wbb')
for key in d:
    print key, d[key]

for k, v in d.items():
    print k, '=', v
print [k + '=' + v
       for k, v in d.items()]

L1 = ['hello', 'world', 'hhha', 12, None]
L2 = [s.upper() for s in L1 if isinstance(s, str)]
print L2
