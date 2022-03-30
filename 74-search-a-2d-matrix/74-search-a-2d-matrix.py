class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # if we simply can represent this 2D array as a linear list we see that it is actually sorted
        
        # logic for a 3X3 matrix in a lineqr list indices vary from 0-8
        
        # linear index = Totalcol * row+col (i.e n*i+j) for [0][0]= 3*0+0 for [0][1]=3*0+1
        
        # reverse logic:-  row = linear index/totalcol and col = linear index%totalcol
        
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows*cols-1
        
        while start<=end:
            mid = (start+end)//2
            row = mid//cols
            col = mid%cols
            
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col]<target:
                start=mid+1
            
            else:
                end=mid-1
        
        
        return False
    
    #O(logm+logn)
        