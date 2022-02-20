class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # using 2 pointer
        
        left, right = 0, 1
        max_profit = 0
        
        while(right!=len(prices)):
            if prices[right]>prices[left]:
                profit = prices[right]-prices[left]
                max_profit = max(profit, max_profit)
                right+=1
            
            elif prices[right]<=prices[left]:
                left = right
                right+=1
        
        return max_profit
        