class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n = len(arr)
        remove = n // 20

        s = arr[remove : n-remove]
        return float(sum(s)) / len(s)