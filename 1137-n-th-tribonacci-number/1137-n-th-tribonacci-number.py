class Solution(object):
    def tribonacci(self, n):
        memo = {}
        def tb(n):
            if n == 0: return 0
            if n == 1 or n == 2: return 1
            if n in memo: return memo[n]
            else:
                memo[n] = tb(n-1) + tb(n-2) + tb(n-3)
                return memo[n]
        return tb(n)