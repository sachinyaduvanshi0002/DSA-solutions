class Solution(object):
    def singleNumber(self, nums):
        
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        for i in freq:
            if freq[i] == 1:
                return i