class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        # O(N2)
        
        # basically we can have 2^n different numbers and there are only n present
        # so we have many options
        
        # we only have to comapre  n+1 time to get a number not present
        # also we convert nums to hashset which will take O(n) time
        
        # so O(n2)
        
        s = { n for n in nums}
        
        def backtrack(idx,curr):
            if idx == len(nums):
                res = "".join(curr)
                return None if res in s else res
            
            res= backtrack(idx+1,curr)
            if res:
                return res
            
            curr[idx] ="1"
            res = backtrack(idx+1,curr)
            if res:
                return res
                
        
        
        
        return backtrack(0,["0" for n in nums])
        