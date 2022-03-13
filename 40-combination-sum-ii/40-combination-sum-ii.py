class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Since we have to return the combinations so the time would be O(2^n)
        # basically all elements in the decision tree
        
        # we have to modify the decision tree to avoid duplicates
        # basically when we choose a number in 1 subtree we should ensure that
        # the number doesn’t appear at all in the 2nd sub-tree.This would be difficult
        # if we have numbers spread over so we sort the tree.
        # By doing this we ensure that the number picked in 1 half doesn’t appear in 2nd half
        # and cause duplicates 
        
        candidates.sort()
        
        result = []
        
        def backtrack(curr,idx,target):
            if target == 0:
                result.append(curr.copy()) # we are adding a copy because we will be modifying the curr
            
            if target<0:
                return
            
            prev = -1 # to ensure that we don’t add the same element again to avoid duplicates
            # taking -1 as constraint says we'll never have -1
            for i in range(idx,len(candidates)): # so that we go from current index onwards instead of whole array
                if candidates[i] == prev:
                    continue # skip if we are adding the same element
                curr.append(candidates[i])
                backtrack(curr,i+1,target-candidates[i])
                curr.pop()
                
                prev=candidates[i]
        
        backtrack([],0,target)
        return result
        