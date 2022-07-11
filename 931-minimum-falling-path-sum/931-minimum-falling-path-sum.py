class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # recurrence relation for cell 
        # f(i,j) = min(matrix[row-1][col-1],matrix[row-1][col],matrix[row-1][col+1])
        
        # for a little less hastle we will add 2 extra cols 1 in front and other in end to reduce extra code
        # see diagram here:- https://leetcode.com/problems/minimum-falling-path-sum/discuss/186689/Java-DP-solution-with-graph-illustrated-explanations
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # so basically what it helps us do is maitain max at the corner of first and last column saving us hastle of edge cases for first and last column
        dp =[[float("inf") for _ in range(cols+2)] for _ in range(rows)]
        
        for i in range(1,cols+1):
            dp[0][i]=matrix[0][i-1]
        
        
        for i in range(1,rows):
            for j in range(1,cols+1):
                dp[i][j]= min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+matrix[i][j-1]
        
        
        # the minium of the last row will be our answer
        return min(dp[-1])
    
    # Time: O(MN)
    # Space: O(MN)
        