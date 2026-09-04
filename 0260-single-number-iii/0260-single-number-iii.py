class Solution(object):
    def singleNumber(self, nums):
        
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        ans = []
        for i in nums:
            if freq[i] == 1:
                ans.append(i)

        return ans