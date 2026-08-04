class Solution:
    def isStrong(self, n):
        # code here
        temp = n
        sumf = 0
        while n > 0:
            digit = n % 10
            
            fact = 1
            for i in range(1, digit + 1):
                fact = fact * i
                
            sumf = sumf + fact
                
            n = n // 10
        
        if sumf == temp:
            return True
        else: return False