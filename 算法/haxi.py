class Solution:
    dic = dict()

    def checkOnce(self, l):
        for i in l:
            value = self.dic.get(i, 0) + 1
            self.dic[i] = value

        l = list()
        for (k, v) in self.dic.items():
            if v == 1:
                l.append(k)

        return l


print Solution().checkOnce([1, 2, 3, 2, 2])
