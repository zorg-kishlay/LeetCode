class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # typical dfs problem
        
        def dfs(i,j):
            
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:
                return 0
            
            current=1
            grid[i][j]=0
            
            for (x,y) in [(0,1),(0,-1),(1,0),(-1,0)]:
                current+= dfs(i+x,j+y)
            return current
        
        
        for i in range(rows):
            for j in range(cols):
                #if grid[i][j]==1:
                #current=dfs(i,j)
                result=max(result,dfs(i,j))
        
        
        return result
        