class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # O(N) greedy approach
        # instead of thinking from start we can think from end
        # for e.x [2,3,1,1,4] so we have to reach 4 which is our end goal
        # we can reach 4 from 1(second last index) so we just need to check if we can reach
        # 1 so our end keeps on coming forward
        
        end = len(nums)-1
        
        # starting from last index
        
        for idx in range(len(nums)-1,-1,-1):
            if idx + nums[idx] >= end:
                end = idx
        
        # if we can reach at the start then end should be at 0
        
        return True if end==0 else False
        