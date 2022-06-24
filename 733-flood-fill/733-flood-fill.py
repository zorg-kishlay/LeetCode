class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        old_colr = image[sr][sc]
        
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or image[i][j]==color or image[i][j]!=old_colr:
                return
            
            image[i][j]=color
            
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(i+x,j+y)
        
        dfs(sr,sc)
        
        return image
        