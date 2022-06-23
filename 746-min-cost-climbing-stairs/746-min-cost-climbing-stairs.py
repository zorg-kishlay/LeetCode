class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # IK
        
        n = len(cost)
        table = [0]* (n+2)
        cost.append(0)
        table[1]=cost[0]
        
        for i in range(2,n+2):
            table[i]=cost[i-1]+min(table[i-1],table[i-2])
        
        
        return table[n+1]
        
# Time and Space: O(N)