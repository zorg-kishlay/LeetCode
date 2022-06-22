class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # total no of paths = C(m+n-2,m-1)
        table= [[0 for _ in range(n)] for _ in range(m)]
        
        # for 0th row and cloumn we have only 1 way to reach them either right or bottom
        for i in range(m):
            table[i][0]=1
            
        for i in range(n):
            table[0][i]=1
        
        
        for i in range(1,m):
            for j in range(1,n):
                table[i][j]=table[i-1][j]+table[i][j-1]
        
        return table[m-1][n-1]
        
        
        # Time and Space:- O(mn) can improve space by only storing 2 rows or cols based on m and n values