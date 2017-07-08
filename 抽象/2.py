class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        self.A = A
        self.A.sort()
        print self.A


a = Solution()
a.sortIntegers2([3, 2, 1, 4, 5])
