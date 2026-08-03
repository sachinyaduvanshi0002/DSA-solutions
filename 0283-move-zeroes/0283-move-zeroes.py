class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        x = 0
        for y in range(n):
            if nums[y] != 0:
                nums[x], nums[y] = nums[y], nums[x]
                x += 1