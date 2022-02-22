class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # defaul case when len(nums)=1
        result = max(nums)
        
        currentMax, currentMin = 1,1
        
        for num in nums:
            
            # for case when num =0 we would reset our max and min to
            # default values 1( in our case)
            
            if num == 0:
                currentMax, currentMin = 1,1
                continue
            
            temp = num*currentMax # since we will be updating current max and need the older value later
            # this can be current num*currentMax(positive)
            # or num*currentMin (for negatives) or num
            # [-1,8]
            currentMax = max(num*currentMax,num*currentMin, num )
            currentMin = min(temp,num*currentMin, num )
            
            result = max(currentMax,currentMin,result )
        
        return result
        