# coding = utf-8
def ipCheck(ip):
    ipList = ip.strip().split('.')
    l = len(ipList)
    if l != 4:
        return False
    try:
        for i in ipList:
            i = int(i)
            if i not in range(0, 255):
                return False
    except:
        return False
    return True


ip = 'hhhh'
print ipCheck(ip)
