class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        
        def helper(res,index,slate):
            if res<0 or len(slate)>k:
                return
            
            # root node worker
            if res ==0 and len(slate)==k:
                result.append(slate[:])
                return
            
            
            
            # internal node worker
            for i in range(index,10): # since 9 is the max value of integer
                slate.append(i)
                helper(res-i,i+1,slate)
                slate.pop()
        
        helper(n,1,[])
        return result
        