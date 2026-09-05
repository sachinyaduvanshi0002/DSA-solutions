class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n = len(arr)
        remove = n // 20

        s = 0
        for i in range(remove, n-remove):
            s += arr[i]

        return float(s) / (n - 2*remove)