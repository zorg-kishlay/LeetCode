class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]==1:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        table = [[0 for _ in range(cols)] for _ in range(rows)]
        table[0][0]=1 if not grid[0][0] else 1 # If possible to reach starting node
        
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]:
                    
                    if i-1>=0:
                        table[i][j]+=table[i-1][j]
                    
                    if j-1>=0:
                        table[i][j]+=table[i][j-1]
        
        
        return table[-1][-1]
        
        # Time and Space :- O(mn)