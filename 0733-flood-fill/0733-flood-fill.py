class Solution(object):
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]

        if old == color:
            return image
        
        def dfs(l, r):

            if l<0 or l>=len(image) or r<0 or r>=len(image[0]):
                return

            if image[l][r] != old:
                return
            image[l][r] = color
            
            dfs(l-1, r)
            dfs(l, r-1)
            dfs(l+1, r)
            dfs(l, r+1)

        dfs(sr, sc)
        return image