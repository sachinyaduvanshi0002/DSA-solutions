class Solution(object):
    def smallestNumber(self, n, t):
        
        for i in range(n, n + 10):
            temp = i
            pdt = 1
            while temp > 0:
                d = temp % 10
                pdt = pdt * d
                temp = temp // 10
            
            if pdt % t == 0:
                return i