class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2^t) where t is the target
        
        
        
        result = []
        
        def dfs(i,current,total):
        #                                []
        #
        #                   [2]                     []
        #
        #           [2,2]               [2]         [3]             []
        #
        #   [2,2,2]    [2,2,3]     [2,3]     [2]
        #
        #
        # Breaks when total>target 
        #
            if target == total:
                # since we will be updating the current list
                result.append(current.copy())
                return
            
            if  i>=len(candidates) or total > target:
                return
            
            # we have 2 options to either select the current index
            # or not select the point to avoid duplication
            
            current.append(candidates[i])
            # since we are choosing this
            dfs(i,current,total+candidates[i])
            
            current.pop()
            # when we are not selecting the current item
            dfs(i+1,current,total)
        
        dfs(0,[],0)
        return result
        