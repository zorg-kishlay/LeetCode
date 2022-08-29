class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # we will do dfs and edit the existing matrix
        # this problem is similar to number of connected components in graph
        
        
        rows = len(grid)
        cols = len(grid[0])
        noOfIslands = 0
        
        def changeNegh(row,col):
            if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]!="1":
                return
            grid[row][col]="X"
            for x,y in (1,0),(0,1),(-1,0),(0,-1):
                changeNegh(row+x,col+y)
            
        
        
        
        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col]=="1":
                    noOfIslands+=1
                    changeNegh(row,col)
        
        
        return noOfIslands