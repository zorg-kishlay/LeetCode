class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        dp = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                
                # last box is our target and the min sum there is the value itself
                if i == rows-1 and j == cols-1:
                    dp[i][j] = grid[i][j]
                
                # basically for elements at last row and last col we don't have option to move
                
                
                # last row
                elif i == rows-1:
                    dp[i][j] = dp[i][j+1]+grid[i][j]
                    
                # last column
                elif j == cols-1:
                    dp[i][j] = dp[i+1][j]+grid[i][j]
                
                # now for all other elements we have an option to choose from down and left
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1])+grid[i][j]
        
        
        # our result sum will be at the first box
        return dp[0][0]