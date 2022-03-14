class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # basic approach would be to find the number in the array and then apply 2 pointer
        # to traverse it
        
        # we can use binary search since the array is sorted but the element might not exist in the array
        
        # what we'll do if ekement doesn’t exist then we will choose the closest value to the number
        
        l, r = 0, len(arr) - 1
        
        # Find index of x or the closest val to x
        val, idx = arr[0], 0
        while l <= r:
            m = (l + r) // 2
            curDiff, resDiff = abs(arr[m] - x), abs(val - x)
            if (curDiff < resDiff or 
                (curDiff == resDiff and arr[m] < val)):
                val, idx = arr[m], m

            if arr[m] < x:    l = m + 1
            elif arr[m] > x:  r = m - 1
            else:             break
    
        l = r = idx                
        for i in range(k - 1):
            if l == 0:           
                r += 1
            elif r == len(arr) - 1 or x - arr[l-1] <= arr[r+1] - x:               
                l -= 1
            else:
                r += 1        
        return arr[l:r+1]