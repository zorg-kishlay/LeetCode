class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        start = 0
        end = len(height)-1
        capacity = 0
        
        # we will traverse using 2 pointers capacity = height(min of the 2 pointers water will overflow otherwise) * width(between 2 pointers)
        
        while(start<end):
            width = end-start # calculating the y axis
            current_capacity = min(height[start],height[end]) * width
            
            capacity = max(capacity,current_capacity)
            
            # we will increase pointer based on the lower height
            if height[start]<height[end]:
                start+=1
            
            else:
                end-=1
        
        
        return capacity
    
    # Time O(N)