class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # sum of n digits is (n*(n+1))/2
        # so subtarcting actual sum with expected should
        # give us answer
        
        n = len(nums)
        expected = (n*(n+1))//2
        
        actual = 0
        
        for ele in nums:
            actual+= ele
            
        
        return expected - actual
        