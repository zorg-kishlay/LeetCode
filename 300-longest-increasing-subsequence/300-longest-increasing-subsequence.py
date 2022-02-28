class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # DP soln :- O(n2)
        
        # max inc subseq for last digit is 1
        # MIS for last-1 is max(1(i.e itself), MIS(last)+1(only if last>last-1))
        # similary for last-2 it is either 1 or 1+MIS(last-1) or MIS(last)+1
        
        
        lis = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)): # check for elments after current
                
                if nums[j]>nums[i]:
                    lis[i] = max(lis[i],1+lis[j])
        
        return max(lis)
        
        
        