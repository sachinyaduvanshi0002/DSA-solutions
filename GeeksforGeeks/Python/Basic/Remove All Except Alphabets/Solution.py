class Solution:
    def removeChars(self, s: str) -> str:
        # code here
        res = ""
        for ch in s:
            if ch.isalpha(): res += ch
        return res