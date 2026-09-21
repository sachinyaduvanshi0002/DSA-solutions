class Solution(object):
    def maxCount(self, m, n, ops):
        minRow = m
        minCol = n

        for a,b in ops:
            minRow = min(minRow, a)
            minCol = min(minCol, b)

        return minRow * minCol