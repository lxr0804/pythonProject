people={
    'liuxr':{
        'phone':'18614028606',
        'addr': 'qd'
    },
    'wbb':{
        'phone':'13269528633',
        'addr':'dz'

    }
}
data = {
    'liuxr': 123,
    'wbb' : 232
}
print "wbb's phone is %(wbb)s" % data

name = dict(a='liuxr', b='wbb')
print people.get('liuxr')