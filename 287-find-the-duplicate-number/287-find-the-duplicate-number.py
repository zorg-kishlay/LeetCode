class Solution:
    # https://www.youtube.com/watch?v=wjYnzkAhcNk&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=42
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast =0
        
        while True:
            slow = nums[slow]
            # changing beacuse initially slow and fast are at same postion
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                break
        
        return slow
        