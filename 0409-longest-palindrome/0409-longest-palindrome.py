class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        ans = 0
        odd = False
        for j in freq:
            if freq[j] % 2 == 0:
                ans += freq[j]
            else: 
                ans += freq[j] - 1
                odd = True
        
        if odd:
            ans += 1
        
        return ans