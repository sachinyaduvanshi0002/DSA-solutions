class Solution:
    def convertFive(self, n):
        # code here
        n = str(n)
        ans = ""
        for i in n:
            if i == "0":
                ans += "5"
            else: ans += i
        return int(ans)