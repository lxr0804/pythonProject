class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        le = len(s)
        if le == 0 or le == 1:
            return le

        max_len = 0
        z = set()
        for i in range(0, le):
            z.add(s[i])
            length = 0
            for j in range(i + len(z), le):
                l = len(z)
                z.add(s[j])
                length = len(z)
                if len(z) == l:
                    z.remove(s[i])
                    break
            if length > max_len:
                max_len = length
        return max_len

print Solution().lengthOfLongestSubstring('dkjarinvfjhruegfdjkvnfdjahvufevnfdnvjfhvgufejdvfda')