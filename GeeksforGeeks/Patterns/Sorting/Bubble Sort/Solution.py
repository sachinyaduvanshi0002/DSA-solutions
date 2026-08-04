class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for j in range(n):
            for i in range(0, n-j-1):
                if arr[i] >arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr