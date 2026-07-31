class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        push = 1
        res = 0

        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        
        s = sorted(freq.values(), reverse=True)

        while len(s) > 0:
            take = min(8, len(s))
            for ch in range(take):
                res += push * s[ch]
            
            s = s[take:]
            push += 1
        return res