class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # looks like maths
        # basically its increasing sum where total sum = n
        
        # r/2*(r+1) = n
        left,right = 1,n
        result = 0
        
        while(left<=right):
            mid = (left+right)//2
            rows = (mid/2)*(mid+1)
            
            if rows>n:
                right =mid-1
            
            else:
                left = mid+1
                result = max(result,mid) # since we want to find the maximum
        
        return result
        