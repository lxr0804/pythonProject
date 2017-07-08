# coding=utf-8

database = [
    ['liuxr', '1234'],
    ['wangbb', '23124']
]

name = raw_input('Enter your name:')
pin = raw_input('Enter your pin:')
if [name, pin] in database:
    print 'welcome'
