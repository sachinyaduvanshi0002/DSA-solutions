class Solution:
    def smallerAndLarge(self, s: str) -> list[str]:
        # code here
        
        minlen = 10**5
        maxlen = 0
        
        small = ""
        large = ""
        
        s = s.split()
        
        for word in s:
            if len(word) < minlen:
                small = word
                minlen = len(word)
                
            if len(word) >= maxlen:
                large = word
                maxlen = len(word)
                
        return [small, large]