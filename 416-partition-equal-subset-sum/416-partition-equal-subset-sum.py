class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # for solution to exist the sum of all elements in the list should be even
        # odd+odd = even # if they are same then both would either be odd or even
        # even+even = even
        
        @cache # here dp array will be dp[idx][sum]
        def subsetSum(suma,idx):
            if suma==0:
                return True
            if idx>=len(nums) or suma<0:
                return False
            
            # check sum with ele and without it
            return subsetSum(suma-nums[idx],idx+1) or subsetSum(suma,idx+1)
        
        suma=sum(nums)
        return suma &1 ==0 and subsetSum(suma//2,0)
    
    #space O(N*sum) and time O(N*sum)
        
        