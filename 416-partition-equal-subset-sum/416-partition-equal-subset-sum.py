class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # dp problem think of subset problem
# recurrence relation f(i)= f(i+1,halfsum-nums[i]){include} or f(i+1,halfsum){exclude}

# we need 2 equal sum subsets now that is possible only when the sum is even why? odd+odd = even or even+even = even

# so we can check for sum/2 to exist in any of the subsets as exclude covers the other subset
        
        total=sum(nums)
        if total%2!=0:
            return False
        
        halfsum = total//2
        rows = len(nums)+1
        cols = halfsum+1
        
        # we have 2 changin params index(i) and currentSum so it is a 2D Dp problem
        
        dp = [[False for _ in range(cols)] for _ in range(rows)]
        
        # base case when halfsum =0 we will have a true that is 2 empty subsets as answers
        # and when index = len(nums) we would have selected all elements and can form the sum with the giuven set so it will be false
        
        for i in range(rows):
            dp[i][0]=True
        
        for j in range(1,cols):
            dp[rows-1][j]=False
        
        
        # we know according to recurrence relation that current cell value will depend upon next_row(i+1) and previous column(halfsum-nums[i])
        
        for i in range(len(nums)-1,-1,-1):
            for su in range(1,cols):
                result = False
                
                if su >= nums[i]:
                    result = dp[i+1][su - nums[i]]
                
                dp[i][su]= result or dp[i+1][su]
        
        return dp[0][halfsum]
            
        