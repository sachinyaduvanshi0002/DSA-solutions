class Solution:
    def countFactors (self, n):
        # code here
        count = 0
        i = 1
        
        while i * i <= n:
            if n % i == 0:
                if i == n // i:
                    count += 1
                else:
                    count += 2
            i += 1
        return count