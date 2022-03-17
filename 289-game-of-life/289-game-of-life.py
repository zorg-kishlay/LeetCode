class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # for O(MN) space and time take a MN matrix and change values in it
        
        # for a O(1) space we try to make a binary number out of old and new values
        
        # old   new     value
        # 0     0          0
        # 1     0           1
        # 0     1           2
        # 1     1           3
        
        rows , columns = len(board), len(board[0])
        
        def findNeighbours(r,c):
            neighbours = 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    
                    if (i==r and j==c) or i== rows or j == columns or i<0 or j<0:
                        continue
                    if board[i][j] in [1,3]:
                        neighbours+=1
            return neighbours
                        
        
        for row in range(rows):
            for column in range(columns):
                neighbours = findNeighbours(row,column)
                
                if board[row][column]:
                    if neighbours in [2,3]:
                        board[row][column] = 3
                elif neighbours ==3:
                    board[row][column] = 2
        
        # now changing back the board to 0 and 1
        
        for row in range(rows):
            for column in range(columns):
                if board[row][column] ==1:
                    board[row][column] = 0
                elif board[row][column] in [2,3]:
                    board[row][column] = 1
                    
                
        