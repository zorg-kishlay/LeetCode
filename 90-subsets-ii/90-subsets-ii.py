class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        
        def helper(arr,index,slate):
            
            if index == len(nums):
                new_num=sorted(slate[:])
                if new_num not in result:
                    result.append(new_num)
                return
            
            # intenal node workers
            
                        # choice of rejecting current element
            helper(arr,index+1,slate)
            
            # choice of choosing current element
            slate.append(arr[index])
            helper(arr,index+1,slate)
            slate.pop()
            

        
        
        helper(nums,0,[])
        return result
            
            