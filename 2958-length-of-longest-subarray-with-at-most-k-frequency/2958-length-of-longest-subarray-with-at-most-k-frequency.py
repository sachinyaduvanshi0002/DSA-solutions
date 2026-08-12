class Solution(object):
    def maxSubarrayLength(self, nums, k):
        ans = 0
        left = 0
        freq = {}

        for curr in range(len(nums)):
            freq[nums[curr]] = freq.get(nums[curr], 0) + 1

            while freq[nums[curr]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            ans = max(ans, curr - left + 1)

        return ans