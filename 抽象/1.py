class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        self.n = n
        self.seq = [0, 1]
        for i in range(8):
            self.seq.append(self.seq[-2] + self.seq[-1])
        return self.seq[n - 1]



a = Solution()
a.fibonacci(1)
