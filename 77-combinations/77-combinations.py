class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # This is basically a backtracking problem with the constraint being size of slate
        
        
        result = []
        
        def helper(s,i,slate):
            # backtracking case
            # here we check for constraint
            if len(slate)==k:
                result.append(slate[:])
                return # this helps us in overcoming the case where lenght(slate)>k as that case is never reached
            
           
        # we reach here only when len(slate)<k
            # leaf case
            # doesn't matter if leaf or internal the slate copy command is taken care at the backtracking case so we just return here
            if len(s)==i: # returning from leaf node
                return
            
            
            
            #internal node worker case
            # same as subsets we have 2 options include and exclude
            
            helper(s,i+1,slate) # exclude
            
            # include case
            slate.append(s[i])
            helper(s,i+1,slate)
            slate.pop()
        
        input =[]
        for idx in range(1,n+1):
            input.append(idx)
        helper(input,0,[])
        return result
        