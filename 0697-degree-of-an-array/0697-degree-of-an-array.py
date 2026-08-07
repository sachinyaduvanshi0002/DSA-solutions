class Solution(object):
    def findShortestSubArray(self, nums):
        fir = {}
        last = {}
        freq = {}

        for i, num in enumerate(nums):
            if num not in fir:
                fir[num] = i
            
            last[num] = i

            freq[num] = freq.get(num, 0)+1

        degree = max(freq.values())

        ans = len(nums)

        for num in freq:
            if freq[num] == degree:
                ans = min(ans, last[num] - fir[num] + 1)

        return ans