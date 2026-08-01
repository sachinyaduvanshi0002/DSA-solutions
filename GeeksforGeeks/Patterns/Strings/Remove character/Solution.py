class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        res = ""
        for ch in str1:
            if ch in str2: continue
            else: res += ch
        return res