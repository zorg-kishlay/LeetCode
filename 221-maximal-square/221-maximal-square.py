class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        row = len(matrix)
        column = len(matrix[0])
        
        dp =[[0 for _ in range(column)]  for _ in range(row)]
        
        max_side = float("-inf")
        
        for i in range(row-1,-1,-1):
            for j in range(column-1,-1,-1):
                
                if i == row-1 and j == column-1:
                    dp[i][j] = int(matrix[i][j])
                elif i== row-1 or j==column-1:
                    dp[i][j] = int(matrix[i][j])
                
                else:
                    if matrix[i][j] == '0':
                        dp[i][j] = 0
                    
                    else:
                        dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
                max_side = max(max_side,dp[i][j])
        
        
        return max_side * max_side
        