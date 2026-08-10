class Solution(object):
    def islandPerimeter(self, grid):
        def dfs(l, r):
            if l<0 or l>=len(grid) or r<0 or r>=len(grid[0]):
                return 1
            
            if grid[l][r] == 0:
                return 1

            if grid[l][r] == -1:
                return 0

            grid[l][r] = -1

            return(dfs(l-1, r) + dfs(l+1, r) + dfs(l, r-1) + dfs(l, r+1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)