class Solution(object):
    def majorityElement(self, nums):

        can1 = None
        can2 = None
        c1 = 0
        c2 = 0

        for x in nums:
            if x == can1:
                c1 += 1
            elif x == can2:
                c2 += 1
            elif c1 == 0:
                can1 = x
                c1 = 1
            elif c2 == 0:
                can2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
            
        ans = []
        n = len(nums) / 3

        for c in [can1, can2]:
            if nums.count(c) > n:
                ans.append(c)

        return ans