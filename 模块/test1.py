# coding=utf-8
def ipCheck(ip):
    ipList = ip.strip().split('.')
    l = len(ipList)
    if l != 4:
        return False

    for i in ipList:
        try:
            j = int(i)
            if j not in range(0, 255):
                return False
        except:
            return False

    return True


ip = '哈哈'
print ipCheck(ip)
