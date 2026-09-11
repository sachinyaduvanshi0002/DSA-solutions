class Solution(object):
    def majorityElement(self, nums):

        freq = {}
        for x in nums:
           freq[x] = freq.get(x, 0) + 1

        n = len(nums) / 3
        
        ans = []
        for c in freq:
            if freq[c] > n:
                ans.append(c)
        
        return ans