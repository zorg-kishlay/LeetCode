class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result =[]
        
        # base case when we have just one 1 element
        if len(nums) == 1:
            return [nums[:]] # since we need to return a list of list
        
        for idx in range(len(nums)):
            
            # we remove the first element to check for a smaller solution
            # so for [1,2,3] we remove 1 and send [2,3]
            removed = nums.pop(0)
            
            perms = self.permute(nums)
            
            # so perms will have [2,3] and [3,2] now we need to append
            # the popped value to both of them to have the complete permutation
            
            for perm in perms:
                perm.append(removed)
            result.extend(perms)
            nums.append(removed)
        return result
        