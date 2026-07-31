class Solution(object):
    def minimumPushes(self, word):

        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        
        arr = sorted(freq.values(), reverse=True)

        res = 0
        for ch in range(len(arr)):
            res += arr[ch] * (ch // 8 + 1)
        
        return res