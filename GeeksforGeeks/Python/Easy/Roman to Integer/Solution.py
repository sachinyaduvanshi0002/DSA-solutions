class Solution:
    def romanToInteger(self, s): 
        # code here
        intv = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        ans = 0
        
        for i in range(len(s) - 1):
            if intv[s[i]] < intv[s[i+1]]:
                ans -= intv[s[i]]
                
            else: ans += intv[s[i]]
            
        ans += intv[s[-1]]
        
        return ans