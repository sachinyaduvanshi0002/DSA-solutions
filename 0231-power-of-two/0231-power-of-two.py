class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1: return False
        while n % 2 == 0:
            n = n / 2
        return n == 1

        # return n > 0 and (n & (n-1) == 0)