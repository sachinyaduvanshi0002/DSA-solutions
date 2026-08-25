class Solution(object):
    def missingMultiple(self, nums, k):
        ok = k
        while k in nums:
            k += ok
        return k