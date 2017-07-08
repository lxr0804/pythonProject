def charcontact(str1, str2):
    str = str1 + str2
    print str


def charcontact2(str1, str2):
    list = [str1, str2]
    str = ''
    str.join(list)

    print str.join(list)


charcontact('he', 'llo')
charcontact2('he', 'llo')
