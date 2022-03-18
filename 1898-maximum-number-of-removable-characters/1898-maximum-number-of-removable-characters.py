class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        # Time O(NlogK) where K is the size of removable array
        # we will maintain a set of removed indices
        def isSub(s,sub):
            idx1,idx2= 0,0
            
            while idx1<len(s) and idx2<len(sub):
                if idx1 in removed or s[idx1]!= sub[idx2]: # we increase index of the main string
                    idx1+=1
                    continue
                
                idx1+=1
                idx2+=1
                
            return idx2 == len(sub) # if we have found the sub-seq we'll have found it in main string
        
        
        result = 0
        left,right=0,len(removable)-1
        while left<=right:
            mid = (left+right) //2
            removed=set(removable[:mid+1]) # basically index upto mid 1
            if isSub(s,p):
                result = max(result,mid+1)
                left = mid+1
                
            else:
                right = mid-1
        
        return result
                    
        