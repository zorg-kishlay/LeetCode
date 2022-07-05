class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set()
        
        # add all elements to the set to get rid of duplicate elements
        for num in nums:
            num_set.add(num)
        
        longest_seq=0 # to store the final result
        
        # we need to check for 2 sequences 
        # 1. decreasing subsequence with current number being at the end
        # 2. Increasing with current number at start
        # adding both of them will cover the part where current number is in b/w
        
        
        
        for num in nums:
            index,current_len=1,1 # considering element as first
            
            while num-index in num_set:
                current_len+=1
                
                num_set.remove(num-index)# to ensure we don't count it again
                index+=1
            
            # when we reach here we get length of sbsequence of elements less than current
            
            # now for elements greater than num
            index=1
            
            while num+index in num_set:
                current_len+=1
                num_set.remove(num+index)
                index+=1
            
            longest_seq = max(longest_seq,current_len)
        
        
        return longest_seq
            
            
                
            
        