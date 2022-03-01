class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # O(n)
        
        # check for patterns in binary rep
        # and relation between most significant bit and dp array
        dp = [0] * (n+1)
        offset =1
        
        for i in range(1, n+1):
            dp[i] = dp[i // 2] + i%2
        
        
        return dp