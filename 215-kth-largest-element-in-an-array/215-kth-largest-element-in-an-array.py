class Solution:
    
    # Time O(N)
    def quickselect(self,nums,start,end,k):
        
        # base case
        if start == end:
            return
        
        # we pick up the random number to pivot on
        pivot = random.randint(start,end)
        
        # swap start with pivot element
        nums[start],nums[pivot]=nums[pivot],nums[start]
        marker = start # this will help us segregate the areas
        
        for i in range(start+1,end+1):
            if nums[i]<=nums[start]:
                marker+=1
                nums[i],nums[marker]=nums[marker],nums[i] # getting all elements less than start to left hand side
        # marker will be the correct position for pivot element
        nums[start],nums[marker]=nums[marker],nums[start]
        
        if marker==k:
            return
        
        elif marker>k:
            return self.quickselect(nums,start,marker-1,k)
        
        else:
            return self.quickselect(nums,marker+1,end,k)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # in sorted array Kth largest element would be at n-k position
        pos = len(nums)-k
        self.quickselect(nums,0,len(nums)-1,pos)
        return nums[pos]
        