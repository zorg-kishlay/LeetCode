class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # simple plain DFS problem pretty similar to 200 No of Islands if you follow the approach of
        # chaging land to water
        
        # Just that here we will need to do 2 loops top-bottom and left-right and find neighbours of Os present there we convert them to any other character. This covers all cases where the element on board shouldn't be X then we can iterate the board and change every other 0 to X
        
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i,j):
            if 0<=i<rows and 0<=j<cols and board[i][j]=="O":
                board[i][j]="&"
                for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                    dfs(i+x,j+y)
        
        # this will cover top and bottom of matrix
        for i in [0,rows-1]:
            for j in range(cols):
                dfs(i,j)
        
        # This will check for left and right values
        for i in range(rows):
            for j in [0,cols-1]:
                dfs(i,j)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="&":
                    board[i][j]="O"
        