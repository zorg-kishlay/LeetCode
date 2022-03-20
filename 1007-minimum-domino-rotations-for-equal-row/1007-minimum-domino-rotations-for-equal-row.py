class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        # basically for any number to be present in all rows of tops or bottoms
        # the count of the number(combined for both tops and bottoms) should be >= len(tops)
        # if this is established we just need to get the minm of count of indices which isn't having this number
        
        # Time O(N) space O(1)
        
        size = len(tops)
        result = float("inf")
        for i in range(1,7):
            total_count = 0
            count_absent_in_top =0
            count_absent_in_bottom = 0
            
            for j in range(size):
                if tops[j] == i or bottoms[j]==i:
                    total_count+=1
                
                    if tops[j] != i:
                        count_absent_in_top+=1
                
                    if bottoms[j]!=i:
                        count_absent_in_bottom+=1
            
            if total_count>= size:
                result = min(result,count_absent_in_bottom,count_absent_in_top)
        
        
        if result == float("inf"):
            return -1
        
        
        return result
            
            
                    
                
                
            