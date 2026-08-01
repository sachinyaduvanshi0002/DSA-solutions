class Solution:
    def removeSpaces(self, s):
        # code here
        res = ""
        for ch in s:
            if ch in " ": continue
            else: res += ch
        return res