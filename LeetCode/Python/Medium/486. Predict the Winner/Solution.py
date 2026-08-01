class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)
        i = 0
        j = n-1
        def dfs(i, j):
            if i == j:
                return nums[i]
            
            takei = nums[i] - dfs(i+1, j)
            takej = nums[j] - dfs(i, j-1)

            return max(takei, takej)
        return dfs(i, j) >= 0