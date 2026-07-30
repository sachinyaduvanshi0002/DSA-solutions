class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        res = 0
        cost = 1

        while n > 0:
            take = min(8, n)
            for _ in range(take):
                res += cost

            n -= take
            cost += 1
        return res