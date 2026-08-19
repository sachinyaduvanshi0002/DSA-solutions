class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        freq = {}

        for i in range(n - k + 1):
            subarr = set(nums[i:i+k])

            for x in subarr:
                freq[x] = freq.get(x, 0) + 1
        
        ans = []
        for x in freq:
            if freq[x] == 1:
                ans.append(x)

        if not ans: return -1
        else: return max(ans)