class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        xor = 0

        for i in nums:
            xor ^= i

        count0 = nums.count(0)

        if xor != 0:
            return n
        
        if count0 == n:
            return 0

        else: return n-1