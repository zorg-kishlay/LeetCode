class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        # original formula = values[i] + values[j] + i - j
        # can be broken down into values[i]  + i + values[j] - j
        
        # so at each step we would need to check with the maximised values[i]  + i the current values[j] - j
        # and updates the results accordingly
        
        
        result=0
        max_so_far=values[0] # basically values[0]+0 so
        
        for i in range(1,len(values)):
            result = max(result,max_so_far+values[i]-i)
            max_so_far = max(max_so_far,values[i]+i)
        
        
        return result
    
    
    # Time O(N) 
    # Space:- O(1)
        