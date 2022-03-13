class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        # Monotonic increasing stack
        # Ref Video:- https://www.youtube.com/watch?v=YLesLbNkyjA&list=PLot-Xpze53lfOdF3KwpMSFEyfE77zIwiP&index=79
        
        # O(N) time and space
        
        res = 0
        prefix_sum =[0]
        stack = []
        for n in nums:
            prefix_sum.append(prefix_sum[-1]+n)
        
        for i,n in enumerate(nums):
            new_start = i
            while stack and stack[-1][1]>n:
                start,val = stack.pop()
                total = prefix_sum[i]-prefix_sum[start]
                res = max(res,val*total)
                new_start = start
            stack.append((new_start,n))
        
        for start,val in stack:
            total = prefix_sum[len(nums)]-prefix_sum[start]
            res = max(res,val*total)
        
        return res %(10 ** 9+7)
            
                
        