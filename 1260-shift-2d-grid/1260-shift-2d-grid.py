class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        # convert 2d to 1d array and then do operations
        
        # row = row no * no of coln + col no
        
        
        # Time O(MN)
        
        M,N = len(grid),len(grid[0])
        
        def posToVal(r,c):
            return r*N+c
        
        def valToPos(v):
            return [v//N,v%N] # row,col
        
        res =[[0]*N for _ in range(M) ]
        
        for r in range(M):
            for c in range(N):
                val = (posToVal(r,c)+k)% (M*N) # this will give us the val where we want to insert
                newR,newC = valToPos(val)
                
                res[newR][newC]=grid[r][c]
        
        return res