class Solution(object):
    def findDisappearedNumbers(self, nums):
        # s = set(nums)
        # ans = []
        # for i in range(1, len(nums) + 1):
        #     if i not in s:
        #         ans.append(i)
        # return ans


        # s = set(nums)
        # return [i for i in range(1, len(nums) + 1) if i not in s]


        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
            
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans