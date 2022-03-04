class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        # old permutation problem will give us duplicates
        # try drawing decision tree
        
        # with [1,1,2] for first choice only we had 2 duplicates i.e for
        # for first position we were choosing 1 2times which was causing the issue
        # so if we can get rid of the duplicate during our first choice we'll be safe
        
        # we'll use a map for count of digits
        
        num_count = {}
        
        result = []
        perm = []
        
        for num in nums:
            if num not in num_count:
                num_count[num] = 0
            
            num_count[num] += 1
        
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
        
            for num in num_count:
                if num_count[num]>0:
                    perm.append(num)
                    num_count[num] -= 1
                    backtrack()
                    
                    num_count[num] += 1 # add back the count after perm is calculated
                    perm.pop() # remove the appended number
        
        backtrack()
        return result
            