class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)
        memo = {}

        def dfs(l, r):
            if l == r:
                return nums[l]
            
            if (l,r) in memo:
                return memo[(l,r)]

            takel = nums[l] - dfs(l+1, r)
            taker = nums[r] - dfs(l, r-1)

            memo[(l,r)] = max(takel, taker)
            return memo[(l,r)]

        return dfs(0, n-1) >= 0