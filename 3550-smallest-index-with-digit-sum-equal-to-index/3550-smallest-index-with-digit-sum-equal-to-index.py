class Solution(object):
    def smallestIndex(self, nums):
        idx = float('inf')
        for i in range(len(nums)):
            add = 0
            while nums[i] != 0:
                r = nums[i] % 10
                add += r
                nums[i] //= 10
            
            if add == i:
                idx = min(idx, i)

        if idx != float('inf'):
            return idx
        else: return -1