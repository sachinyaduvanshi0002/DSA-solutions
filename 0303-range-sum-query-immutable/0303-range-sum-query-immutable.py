class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        
        return sum