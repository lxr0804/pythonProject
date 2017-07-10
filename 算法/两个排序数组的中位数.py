class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        C = A + B
        D = sorted(C)
        l = len(D)

        if l % 2 == 0:
            i = (l + 1) / 2
            return (D[i - 1] + D[i]) / 2.0
        else:
            i = (l + 1) / 2
            return D[i - 1] / 1.0


a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 4, 5]

x = Solution()
print x.findMedianSortedArrays(a, b)
