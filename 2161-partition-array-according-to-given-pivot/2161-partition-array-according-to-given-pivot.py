class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # for elements less than pivot
        left = []
        
        # for elements greater than pivot
        right = []
        
        # for elements equal to pivot
        pivots = []
        
        for num in nums:
            if num < pivot:
                left.append(num)
            
            elif num > pivot:
                right.append(num)
            
            else:
                pivots.append(num)
        
        return left + pivots + right