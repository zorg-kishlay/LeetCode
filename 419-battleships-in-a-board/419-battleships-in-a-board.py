class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        battelships = 0
        
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i,j):
            
            # base case
            if i<0 or i>= rows or j<0 or j>=cols or board[i][j]!='X':
                return
        
            # editing array in place
            board[i][j]="."
            
            for (x,y) in [(1,0),(0,1)]:
                dfs(i+x,j+y)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='X':
                    battelships+=1
                
                    dfs(i,j)
        
        return battelships