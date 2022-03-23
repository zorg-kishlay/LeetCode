class Solution:
    def maximumSwap(self, num: int) -> int:
        
        # O(N)

        # basically we traverse num from behind find the max element and swap it with
        # left most smallest element which in turn would increase our effort
        
        nums = [int(n) for n in str(num)]
        #max_right = nums[len(nums)-1]
        index_of_max = len(nums)-1
        
        x,y = 0,0
        
        for idx in range(len(nums)-2,-1,-1):
            if nums[idx]>nums[index_of_max]:
                max_right = nums[idx]
                index_of_max = idx
            
            elif nums[idx]<nums[index_of_max]:
                x = idx
                y=index_of_max
        
        # basically swapping biggest value in the right with leftmost small value(not the smallest but the left most)
        nums[x],nums[y]=nums[y],nums[x]
        
        return int("".join([str(n) for n in nums]))
        