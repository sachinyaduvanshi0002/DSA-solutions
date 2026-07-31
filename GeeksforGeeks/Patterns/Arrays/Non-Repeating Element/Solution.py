class Solution:
    def firstNonRepeating(self, arr): 
        freq = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1
        for n in arr:
            if freq[n] == 1:
                return n
        return 0