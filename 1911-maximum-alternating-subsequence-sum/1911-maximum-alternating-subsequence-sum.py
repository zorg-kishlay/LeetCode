class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        # O(N) time and space
        
        dp ={}
        
        def calculate_sum(index,is_even):
            if index == len(nums):
                return 0
            
            if (index,is_even) in dp:
                return dp[(index,is_even)]
            
            # if is even then add else subtract
            total = nums[index] if is_even else (-1)*nums[index]
            # we have 2 options either to take current number or not take it
            # if we take it then we need to add it to sub problem
            # else we can just check for the nect set
            dp[(index,is_even)] = max(total+calculate_sum(index+1,not is_even),calculate_sum(index+1, is_even))
            return dp[(index,is_even)]
        
        return calculate_sum(0,True)