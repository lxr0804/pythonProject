d = dict(name='Liuxr',age=18)
print d
print d['name']
print len(d)
d['age'] = 20
print d
if 'name' in d:
    print "yes"

else:
    print 'false'

s = {
    'name':{
        'name1':'liuxr',
    },
    'age':'12'
}
print s['name']