class Solution(object):
    def checkDivisibility(self, n):
        original = n
        add = 0
        pro = 1

        while n > 0:
            temp = n % 10
            add += temp
            pro *= temp
            n = n // 10

        return original % (add + pro) == 0