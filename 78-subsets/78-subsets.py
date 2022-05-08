class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result =[]
        
        def helper(arr,idx,slate):
            # base case for leaf node
            if idx==len(arr):
                result.append(slate[:])
                return
            
            # for internal worker node there are 2 options choose item at index or not choose
            
            slate.append(arr[idx])
            helper(arr,idx+1,slate)
            slate.pop() # remove whatever added so that the parent will have the access to correct base case
            # not choosing element at idx
            helper(arr,idx+1,slate)
        
        
        helper(nums,0,[])
        return result
            
            
        