class Solution:
    def isPrime(self, n):
        # code here
        if n <= 1: return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True