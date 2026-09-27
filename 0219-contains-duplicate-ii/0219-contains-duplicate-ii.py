class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        freq = {}
        for i, val in enumerate(nums):
            if val in freq and abs(i - freq[val]) <= k:
                return True
            freq[val] = i
        return False