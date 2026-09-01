class Solution(object):
    def searchRange(self, nums, target):

        if not nums: return [-1,-1]

        l = 0
        r = len(nums) - 1
        first = -1
        
        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else: l = mid + 1
        
        l = 0
        r = len(nums) - 1
        last = -1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else: l = mid + 1

        return [first, last]