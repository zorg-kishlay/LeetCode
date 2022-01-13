class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinMin = [float("inf") for i in range(amount+1)]
        
        # for 0 there will be no coins that can make 0 
        coinMin[0] = 0
        for coin in coins:
            for am in range(len(coinMin)):
                # amount can only be formed by coins having value less than or equal to it
                if coin<=am:
                    # adding 1 because we will be adding this coin to make up to the amount
                    #e.x for making 5 we will add 2+3 so we are chosing 3 so 1 is added
                    coinMin[am]=min(coinMin[am],1+coinMin[am-coin])
        
        
        return coinMin[amount] if coinMin[amount]!= float("inf") else -1
                    
            
        