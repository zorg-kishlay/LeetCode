class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 123. -> 231
        # 9153 -> 9315
        
        # we basically traverse from the right and try to find a value for which num[idx]<num[idx+1]
        
        # since if we traverse from left and choose with the smallest value then we will get a greater value but not the next greater value for e.x 123 -> 321
        
        idx = len(nums)-2
        
        while idx>=0 and nums[idx]>=nums[idx+1]:
            idx-=1
        
        
        if idx>=0:
            larger_idx = len(nums)-1
            while nums[idx]>=nums[larger_idx]:
                larger_idx-=1
            nums[idx],nums[larger_idx]=nums[larger_idx],nums[idx]
        
        left,right = idx+1,len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        #nums=nums[idx+1:larger_idx:-1]
        