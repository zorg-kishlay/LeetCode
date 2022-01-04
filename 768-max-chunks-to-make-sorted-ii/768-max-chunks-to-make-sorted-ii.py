import sys
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        
        r_min=[1]*(len(arr)+1)
        r_min[len(r_min)-1]=sys.maxsize
        
        for i in range(len(arr)-1,-1,-1):
            r_min[i]=min(arr[i],r_min[i+1])
        
        left=-sys.maxsize-1
        count=0
        for i in range(len(arr)):
            left=max(arr[i],left)
            
            if(left<=r_min[i+1]):
                count+=1
                
        
        
        
        return count
        