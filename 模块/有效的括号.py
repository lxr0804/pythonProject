class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        x = ['[', '(', '{']
        y = [']', ')', '}']
        z = ['[]', '()', '{}']
        res = []
        for i in s:
            if i in x:
                res.append(i)
            elif i in y:
                if res == []:
                    return False
                else:
                    temp = res.pop(-1)+i
                    if temp not in z:
                        return False
        if len(res)!=0:
            return False
        return True
