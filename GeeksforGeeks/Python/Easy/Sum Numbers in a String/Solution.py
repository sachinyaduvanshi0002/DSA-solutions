class Solution:
    def findSum(self, s):
        # code here
        res = 0
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                res += num
                num = 0
        res += num
        return res