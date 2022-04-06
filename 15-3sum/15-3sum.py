class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort the array to reduce time complexity to O(N2)
        nums.sort()
        result =[]
        #start = 0
        end = len(nums)-1
        
        for idx in range(len(nums)-2):
            
            if idx>0 and nums[idx]==nums[idx-1]: # to skip duplicates
                continue
            left = idx+1
            right = end
            
            while left<right:
                curr_sum = nums[idx]+nums[left]+nums[right]
                
                if curr_sum == 0:
                    result.append([nums[idx],nums[left],nums[right]])
                    
                    # skipping duplicates
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
                
                elif curr_sum < 0:
                    left+=1
                
                else:
                    right-=1
                
        
        
        return result