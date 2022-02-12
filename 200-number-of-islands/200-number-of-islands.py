class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid is None or len(grid)==0:
            return 0
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # 2 steps to be done
                    # 1. Increase island count
                    # 2. Recursively covert adjacent 1's to 0's
                    island_count+=1
                    self.change1_to_0(grid, i, j)
                 
        
        return island_count
        
    
    def change1_to_0(self,grid, i, j):
        # 1. row<0
        # 2. row> grid lenght
        # 3. coulmn < 0
        # 4. column > grid[0] length
        # 5 if grid[i][j] ==0
        
        if i < 0 or i>= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]=='0':
            return
        
        # now we know at i,j is 1
        grid[i][j] = '0'
        # now for all left right bottom positions
        
        self.change1_to_0(grid, i-1, j)
        self.change1_to_0(grid, i+1, j)
        
        self.change1_to_0(grid, i, j-1)
        self.change1_to_0(grid, i, j+1)
        