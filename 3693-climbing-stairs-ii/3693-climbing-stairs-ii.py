class Solution(object):
    def climbStairs(self, n, costs):
        dp = [0] * (n+1)
        dp[0] = 0
        if n >= 1:
            dp[1] = dp[0] + costs[0] + (1-0)**2
        if n>=2:
            dp[2] = min(
                dp[1] + costs[1] + (2-1)**2,
                dp[0] + costs[1] + (2-0)**2
        )
        for i in range(3, n+1):
            dp[i] = min(
                dp[i-1]+costs[i-1]+(i-(i-1))**2,
                dp[i-2]+costs[i-1]+(i-(i-2))**2,
                dp[i-3]+costs[i-1]+(i-(i-3))**2)
        return dp[n]