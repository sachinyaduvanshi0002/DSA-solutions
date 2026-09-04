class Solution(object):
    def singleNumber(self, nums):
        
        ans = []
        for x in nums:
            if nums.count(x) == 1:
                ans.append(x)
        return ans