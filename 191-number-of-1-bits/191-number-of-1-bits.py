class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # we will right shift the number and keep in % 2 which will give 1 if digit is 1 or 0
        
        result = 0
        # O(32) or constant since n will have 32 bits only so O(1)
        while n:
            result += n %2
            n = n >>1 # bit shift by 1
        
        
        return result
        