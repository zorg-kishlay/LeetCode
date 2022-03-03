class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # set 4 boundaries top bottom left and right
        # for smaller sub problems we just need to shift these boundaries by 1
        
        #https://www.youtube.com/watch?v=fMSJSS7eO1w&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=15
        
        left, right = 0, len(matrix[0])-1 # can be len(matrix)-1 as well since nxn matrix
        
        while left < right:
            for i in range(right-left): # 3 interations for 4 rows
                
                # we will use the i to contract the square submatrix
                top, bottom = left, right
                
                # save top left
                top_left = matrix[top][left+i]
                # to reduce the no fo temporary variable we would need
                matrix[top][left+i] = matrix[bottom-i][left] # move 7 to 1's postion after saving 1
                
                
                matrix[bottom-i][left] = matrix[bottom][right-i] 
                
                matrix[bottom][right-i] = matrix[top+i][right]
                
                matrix[top+i][right] = top_left
            right -= 1
            left += 1
                