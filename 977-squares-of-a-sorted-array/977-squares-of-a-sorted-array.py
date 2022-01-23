class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result =[0 for i in range(len(nums))]
        index = len(nums)-1
        start = 0
        end = len(nums)-1
        
        while start<=end:
            start_val = nums[start] * nums[start]
            end_val = nums[end] * nums[end]
            
            if start_val > end_val:
                result[index] = start_val
                start +=1
            
            else:
                result[index] = end_val
                end -=1
            
            index -=1
        
        return result
        