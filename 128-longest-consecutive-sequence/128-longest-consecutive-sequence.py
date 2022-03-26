class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set()
        
        # adding all distinct numbers to the set
        for num in nums:
            num_set.add(num)
        
        longest_result = 0
        # now for each number we just need to check if its consecutive elements are present in
        # the set or not
        
        for num in nums:
            idx,current_longest=1,1
            # for [0,3,7,2,5,8,4,6,0,1]
            # lets have 1 then 0 is present and that length is added to current_longest
            while num-idx in num_set:
                current_longest+=1
                num_set.remove(num-idx) # to ensure same numbers are not counted twice
                idx+=1
            
            idx=1
            
            # we also need to account for the values greater than the current value
            while num+idx in num_set:
                current_longest+=1
                num_set.remove(num+idx)
                idx+=1
            
            longest_result = max(longest_result,current_longest)
        
        return longest_result
                
        