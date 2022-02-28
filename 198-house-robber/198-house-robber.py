class Solution:
    def rob(self, nums: List[int]) -> int:
        
        loot1 ,loot2 = 0,0
        
        # [loot1, loot2, n, n+1]
        # with loot1 we have to choose n but with loot2 we
        # only need loot2 (take it as 3 house problem)
        
        for n in nums:
            temp = max(loot1+n, loot2)
            loot1 = loot2
            loot2 = temp
        
        return loot2
        
        
        