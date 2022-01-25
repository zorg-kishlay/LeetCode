class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        idx = 0
        length = len(arr)
        if length <3:
            return False
        
        while (idx+1<length and arr[idx]<arr[idx+1]):
            idx+=1
            
        if idx==0 or idx==length-1:
            return False
        
        while idx+1 < length and arr[idx] > arr[idx+1]:
            idx+=1
        
        return idx == length-1