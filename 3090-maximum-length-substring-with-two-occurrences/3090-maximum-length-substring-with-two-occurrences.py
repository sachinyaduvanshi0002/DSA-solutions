class Solution(object):
    def maximumLengthSubstring(self, s):
        
        left = 0
        ans = 0
        freq = {}

        for curr in range(len(s)):
            freq[s[curr]] = freq.get(s[curr], 0) + 1

            while freq[s[curr]] > 2:
                freq[s[left]] -= 1
                left += 1
            
            ans = max(ans, curr - left + 1)

        return ans