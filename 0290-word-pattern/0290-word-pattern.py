class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split(" ")

        if len(pattern) != len(s):
            return False

        d1 = {}
        d2 = {}

        for i in range(len(pattern)):
            ch, word = pattern[i], s[i]

            if (ch in d1 and d1[ch] != word) or (word in d2 and d2[word] != ch):
                return False
            
            d1[ch] = word
            d2[word] = ch
        
        return True