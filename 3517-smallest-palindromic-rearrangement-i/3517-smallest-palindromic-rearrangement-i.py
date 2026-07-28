class Solution(object):
    def smallestPalindrome(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        left = ""
        middle = ""

        for ch in sorted(freq):
            left += ch * (freq[ch]//2)
            if freq[ch] % 2 == 1:
                middle += ch
        return left + middle + left[::-1]