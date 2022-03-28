class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # first detail is that we don't have all distinct elments
        
        # like earlier we can't simply discard a part
        
        # overall Logic:- do binary search and we are sure that in each iteration atleast some part of the arrat is sorted
        
        start,end = 0,len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return True
            
            # if the starting and ending elements are same we won't be able to find target
            if nums[start] == nums[mid] and nums[end] == nums[mid]:
                start+=1
                end-=1
            
            elif nums[end]>=nums[mid]:
            # target is in range to right subarray
                if nums[mid]<target and nums[end]>=target:
                    start=mid+1
                else:
                    end=mid-1
            
            # target is in range to left subarray
            else:
                if nums[mid]>target and nums[start]<=target:
                    end=mid-1
                else:
                    start=mid+1
        
        return False
    
    # Time:- worst case O(N) best case O(NlogN)
        