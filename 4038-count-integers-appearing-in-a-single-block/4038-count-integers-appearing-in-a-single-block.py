class Solution(object):
    def countSpecialIntegers(self, nums):
        seen = set()
        d = set()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                if nums[i] in seen:
                    d.add(nums[i])
                else: seen.add(nums[i])
        return len(seen-d)