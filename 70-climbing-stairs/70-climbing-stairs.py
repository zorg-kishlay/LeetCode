class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0]* (n+1)
        return self.climb(n,dp)
    
    def climb(self,n,dp):
        
        if n==0:
            return 1
        
        if n<0:
            return 0
        
        if dp[n]>0:
            return dp[n]
        
        dp[n] = self.climb(n-1,dp) + self.climb(n-2,dp)
        return dp[n]