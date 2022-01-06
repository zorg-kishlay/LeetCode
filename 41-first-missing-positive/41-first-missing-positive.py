class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # 1)Mark elements out of range and check presence of 1
        # 2)Map the elements to their index
        # 3) Find missing positive
        
        
        # var to check prsence of 1
        one = False
        number = len(nums)
        
        for i in range(number):
            if nums[i]==1:
                one = True
            if nums[i]<1 or nums[i]> number:
                nums[i] = 1
        # if One is not present that obviously 1 is missing positive number
        if not one:
            return 1
        
        # Now all numbers should be range in the array
        for i in range(number):
            index = abs(nums[i])
            nums[index-1]= - abs(nums[index-1])
            
        for i in range(number):
            if nums[i]>0:
                return i+1
        
        
        return number+1