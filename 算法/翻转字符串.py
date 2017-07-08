class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        listS = s.strip().split(' ')
        l = len(listS)
        if l == 0 or l == 1:
            return listS[0]
        y = []
        for i in listS[::-1]:
            y.append(i)
        return ' '.join(y)



a = Solution()
print a.reverseWords('hello world')

