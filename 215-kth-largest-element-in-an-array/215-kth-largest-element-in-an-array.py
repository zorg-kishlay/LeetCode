class Solution:
    # O(N) solution
        
    def quickselect(self,nums,start,end,k):
        
        # base case:- for leaf node
        if start==end:
            return
        
        # Lomuto's partioning logc here
        pivot = random.randint(start,end) # to choose a pivot element
        
        # swap pivot with start element so that we can use it to check and swap
        nums[pivot],nums[start]=nums[start],nums[pivot]
        marker_index = start # to mark the index where element at pivot should be
        
        for idx in range(start+1,end+1):
            # if less then we swap it and place it in the starting region
            if nums[idx]<=nums[start]:
                marker_index+=1
                nums[marker_index],nums[idx]=nums[idx],nums[marker_index]
                
            
        # bring pivot element back to its correct position
        nums[start],nums[marker_index]=nums[marker_index],nums[start]
        
        if k ==marker_index: # lucky case we have sorted array for kth element
            return
        
        elif k<marker_index: #we know we need to look for k in the first half
            self.quickselect(nums,start,marker_index-1,k)
        else:
            self.quickselect(nums,marker_index+1,end,k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # logic here is that kth largest element will be present at n-kth position
        indek=len(nums)-k
        self.quickselect(nums,0,len(nums)-1,indek)
        return nums[indek]
        
        
        