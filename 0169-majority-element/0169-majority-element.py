class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        return max(freq, key = freq.get)