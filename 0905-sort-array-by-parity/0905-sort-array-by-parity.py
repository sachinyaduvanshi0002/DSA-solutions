class Solution(object):
    def sortArrayByParity(self, nums):
        res1 = []
        res2 = []
        for x in nums:
            if x % 2 == 0:
                res1.append(x)
            else: res2.append(x)
        return res1+res2