class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for i in freq:
            if freq[i] == 1:
                return i
        return -1