class Solution(object):
    def commonChars(self, words):
        ans = []
        for ch in set(words[0]):
            freq = min(word.count(ch) for word in words)
            
            for _ in range(freq):
                ans.append(ch)
        return ans