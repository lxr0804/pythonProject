class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        l = len(numbers)
        for i in range(0, l):
            for j in range(i+1, l):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i + 1, j + 1]


a = Solution()
print a.twoSum([0, 4, 3, 0], 0)
