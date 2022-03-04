class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # O(M*N) time O(M+N) space
        
        # for O(1) space https://www.youtube.com/watch?v=T41rL0L3Pnw&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=22
        
        column = len(matrix[0])
        row = len(matrix)
        
        column_matrix = [False for _ in range(column)]
        row_matrix = [False for _ in range(row)]
        
        for idx in range(row):
            for jdx in range(column):
                
                if matrix[idx][jdx] == 0:
                    if not row_matrix[idx]:
                        row_matrix[idx] = True
                    
                    if not column_matrix[jdx]:
                        column_matrix[jdx] = True
        
        
        for idx in range(row):
            if row_matrix[idx]:
                for j in range(column):
                    matrix[idx][j] = 0
        
        for idx in range(column):
            if column_matrix[idx]:
                for j in range(row):
                    matrix [j][idx] = 0
                        