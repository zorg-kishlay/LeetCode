class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1]* (amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            minValue = float("inf")
            for coin in coins:
                if i-coin>=0:
                    minValue = min(minValue,dp[i-coin])
            
            dp[i]=minValue+1 # selecting current coin
        
        
        return dp[amount] if dp[amount]!=float("inf") else -1
                
        