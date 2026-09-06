class Solution(object):
    def wordBreak(self, s, wordDict):
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in wordDict and dp[i] == True:
                    dp[j] = True
        
        return dp[len(s)]