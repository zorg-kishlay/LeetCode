class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i=0
        j=len(height)-1
        capacity=0
        
        while(i<j):
            
            width=j-i
            # since the max height of the container would be the lower amongst the two
            capacity=max(capacity,width*min(height[i],height[j]))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
                
        return capacity