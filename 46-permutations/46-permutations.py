class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        # helper to be called recursively to generate permutations
        def helper(s,index,slate):
            # base case for leaf nodes
            
            if index == len(s):
                result.append(slate[:])
                return
            
            # internal node workers
            # check for choices
            
            # choices would be from index to length i.e next element
            
            for pick in range(index,len(s)):
                s[pick],s[index]=s[index],s[pick]
                slate.append(s[index])
                helper(s,index+1,slate)
                slate.pop()
                s[pick],s[index]=s[index],s[pick] # not doing this will result in duplicate entries
        
        
        helper(nums,0,[])
        return result
    
    
    # Time and Space:- O(n!*n)
                
            
        