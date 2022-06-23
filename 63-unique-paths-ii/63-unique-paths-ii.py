class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]==1:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        table = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        table[0][1]=1 # first reachable node i.e starting node
        
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if grid[i-1][j-1]!=1:
                    table[i][j]=table[i-1][j]+table[i][j-1]
        
        
        return table[-1][-1]
        