class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)

        memo = {}

        def dfs(l, r):
            if l == r:
                return piles[l]
            
            if (l, r) in memo:
                return memo[(l, r)]

            takel = piles[l] - dfs(l+1, r)
            taker = piles[r] - dfs(l, r-1)

            memo[(l, r)] = max(takel, taker)

            return memo[(l, r)]

        return dfs(0, n-1) >= 0