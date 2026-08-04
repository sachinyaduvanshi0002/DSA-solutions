class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        n = len(nums)
        l = nums[0]
        r = nums[n-1]
        ans = []
        for i in range(l, r):
            if i not in nums:
                ans.append(i)
        return ans