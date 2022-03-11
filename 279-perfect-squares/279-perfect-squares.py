class Solution:
    def numSquares(self, n: int) -> int:
        
        # lets say we need to solve for 12 and we know answer upto 8
        # so from 8 we need to solve upto 4 and not 12 so the problem can be broken further
        
        dp = [n]* (n+1)
        dp[0] =0
        
        # we stop when the square value is greater than the value we are looking for
        
        # so that operation is bounded by sqrt(n) where n is the number we are looking for
        # so Time O(n*sqrt(n)) and space =O(n)
        
        for target in range(1,n+1):
            for sqr in range(1,target+1): # we stop when sqaure is greater than the number we want to find ways to sqrt(target) basically
                
                square = sqr*sqr
                if target-square<0:
                    break
                
                dp[target] = min(dp[target],dp[target-square]+1) # +1 because we use the current sqaure as well
        
        return dp[n]
                
                
        
        
        
        