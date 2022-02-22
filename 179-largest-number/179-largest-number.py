from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # simple appraoch would be to take 2 numbers
        # and compare there combinations to check which one is bigger
        
        for idx,num in enumerate(nums):
            nums[idx] = str(num)
        
        def compare(n1, n2):
            # since n1 and n2 are strings
            if n1 + n2 > n2 + n1:
                return -1
            
            # doesn't matter if n2 is greater or equal 
            else:
                return 1
        nums=sorted(nums, key =cmp_to_key(compare)) # similar to comparator in Java
        
        result = str(int("".join(nums))) # to handle cases where 000 is output
        return result