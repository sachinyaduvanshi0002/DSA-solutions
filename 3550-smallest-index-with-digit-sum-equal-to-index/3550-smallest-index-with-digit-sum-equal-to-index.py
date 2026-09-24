class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            add = 0
            while nums[i] != 0:
                r = nums[i] % 10
                add += r
                nums[i] //= 10
            
            if add == i:
                return i

        return -1