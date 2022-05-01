class Solution:
    
    def quickselect(self,nums,start,end,index):
        # code executed at leaf when we have only 1 element left
        if start==end:
            return
        
        # Lomuto's partioning
        pivot= random.randint(start,end) # choosing a random pivot
        # swap pivot elemnt with start so that we can compare from start+1
        nums[pivot],nums[start]=nums[start],nums[pivot]
        lower=start
        for num in range(start+1,end+1):
            if nums[num]<=nums[start]:
                lower+=1
                nums[lower],nums[num]=nums[num],nums[lower]
        # to take start to its correct position i.e a position where it is sorted
        nums[start],nums[lower]=nums[lower],nums[start]
        
        if lower==index:
            return
        
        elif lower<index:
            self.quickselect(nums,lower+1,end,index)
        else:
            self.quickselect(nums,start,lower-1,index)
            
        
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums)-k
        
        self.quickselect(nums,0,len(nums)-1,index)
        return nums[index]