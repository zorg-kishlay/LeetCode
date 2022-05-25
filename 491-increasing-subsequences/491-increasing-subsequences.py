class Solution:
    
    def isValidIncSub(self,slate):
        if len(slate)<2:
            return False
        
        for i in range(1,len(slate)):
            if slate[i-1]>slate[i]:
                return False
        
        return True
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = set()
        def helper(s,i,slate):
            
            if i == len(s):
                if self.isValidIncSub(slate):
                    new_num = slate[:]
                    if new_num not in result:
                        result.append(new_num)
                return
            
            helper(s,i+1,slate)
           
            slate.append(s[i])
            #visited.add(s[i])
            helper(s,i+1,slate)
            #visited.remove(s[i])
            slate.pop()
        
        helper(nums,0,[])
        return result
            
        