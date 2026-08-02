class Solution:
    def sumOfAP(self, n, a, d):
        # code here
        ans = 0
        term = a
        for _ in range(n):
            ans += term
            term += d
        return ans