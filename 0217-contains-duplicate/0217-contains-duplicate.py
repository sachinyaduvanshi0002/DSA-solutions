class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else: return True
        return False