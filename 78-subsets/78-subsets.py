class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # O(n*2^n) we will have 2^n subsets and worst case of size n so n*2^n
        
        # decision tree with 2 choices either do or not do there is no try
        
        result = []
        subset = []
        
        def backtrack(i): # i is for the index of the list
            
            if i >= len(nums):
                result.append(subset.copy()) # since we will be modifying the subset list
                return
            
            # when current element is included
            subset.append(nums[i])
            backtrack(i+1)
            
            # when current element is not included
            # since we have already added it so best choice is to remove it
            
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return result
            
        