class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        ways = [0 for coin in range(amount+1)]
        ways[0] = 1
        
        for coin in coins:
            for way in range(len(ways)):
                if coin<=way:
                    ways[way]+= ways[way-coin]
        
        return ways[amount]
        