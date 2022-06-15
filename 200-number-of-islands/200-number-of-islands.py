class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # looks like an alteration of the connected components problem
        
        islands = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def modify_grid(i,j):
            if i< 0 or j< 0 or i>= rows or j>= cols or grid[i][j]=='0':
                return
            
            grid[i][j]='0'
            for diffx,diffy in [(-1,0),(1,0),(0,-1),(0,1)]:
                modify_grid(i+diffx,j+diffy)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    
                    # basically when we find a new component we inc island count
                    islands+=1
                    modify_grid(i,j)
                    
                    # there could have been 2 approaches 1 we maintain a visted array
                    # here we will just modify the neighbours of our rows to 0 so that don't count as
                    # separate islands
        return islands