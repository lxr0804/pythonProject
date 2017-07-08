# coding=utf-8
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
name = raw_input('name:')
key = raw_input('addr or phone:')
#print people['wbb']['phone']

if name in people:
   print "%s's %s is %s" % (name, key, people[name][key])
