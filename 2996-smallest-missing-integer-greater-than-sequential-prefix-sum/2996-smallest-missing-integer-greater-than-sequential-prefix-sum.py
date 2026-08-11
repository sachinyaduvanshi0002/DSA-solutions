class Solution(object):
    def missingInteger(self, nums):
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                ans += nums[i]
            else: 
                break

        while ans in nums:
            ans += 1

        return ans