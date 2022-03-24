class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # DFS backtracking
        
        rows,cols = len(board),len(board[0])
        
        # to avoid revisiting the same box in a particular iteration
        path = set()
        
        def dfs(row,col,curr):
            
            if curr == len(word): # basically we have found every letter in word
                return True
            
            # invalid checks
            
            if row<0 or col<0 or row==rows or col==cols or word[curr]!= board[row][col] or (row,col) in path:
                return False
            
            path.add((row,col))
            # reaching here means we have the character at curr in the board
            res = dfs(row+1,col,curr+1) or dfs(row-1,col,curr+1) or dfs(row,col+1,curr+1) or dfs(row,col-1,curr+1)
            
            path.remove((row,col))
            return res
        
        # we need to call for all positions on the board
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        
        return False
        
# the time is O(N*M)* dfs since dfs function is being called for n*M.
# Now the max complexity of dfs function is 4^len(word) --> because we have 4 diff branches
# O(4^n)
            
        