class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
         # Backtracking try to draw the decision tree then its easy to solve
        
        # basically we can add opening ( only when count("(")<n
        # and we can add ) when count(")")<count("(")
        # so at each step we will have kind of 2 options try drawing decision tree
        # stop adding when count(")") == count("(")
        
        # Using slate method
        
        result = []
        def helper(closed,opened,slate):
            
            if len(slate)==2*n:
                result.append("".join(slate))
                return
            
            # internal node worker
            if opened<n:
                slate.append("(")
                helper(closed,opened+1,slate)
                slate.pop()
            
            if closed<opened:
                slate.append(")")
                helper(closed+1,opened,slate)
                slate.pop()
        
        
        helper(0,0,[])
        return result
        