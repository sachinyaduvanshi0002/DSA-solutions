class Solution:
    def splitString(self, s): 
        # code here 
        s1 = ""
        s2 = ""
        s3 = ""
        for ch in s:
            if ch.isalpha(): s1 += ch
            elif ch.isdigit(): s2 += ch
            else: s3 += ch
        return [s1, s2, s3]