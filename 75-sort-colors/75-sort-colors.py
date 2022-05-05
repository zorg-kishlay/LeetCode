class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    # this we can do using 3-way partioning

    # so we just compare for extremes i.e 0 and 2 and swap only when we encounter them
    
        start,zero_idx=0,0
        end= len(nums)-1

        while start<=end:
            if nums[start]==2: # if we encounter a 2 we move it to the end of the list
                nums[start],nums[end]=nums[end],nums[start]
                end-=1

            elif nums[start]==0: # if we encounter a zero we move it to the starting of the list
                nums[start],nums[zero_idx]=nums[zero_idx],nums[start]
                start+=1
                zero_idx+=1
            else:
                start+=1
            
            
