class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        # take 2 bool values inc and dec traverse the array and check if anyone becomes false
        
        inc = True
        dec = True
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dec = False
            if nums[i]<nums[i-1]:
                inc = False
        
        # the only way this will return false is when both inc and dec are false 
        # that is the array has values less than and greater than next values
        return inc or dec
        