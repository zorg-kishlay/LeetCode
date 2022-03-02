class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # O(N) space and time
        # sliding window
        
        substring_set = set()
        left, result = 0, 0
        
        for right in range(len(s)):
            
            # while we encounter a duplicate character
            # we will pop it out of the set and increase the left pointer
            while s[right] in substring_set:
                substring_set.remove(s[left])
                left += 1
            # not a duplicate we add it to the set
            substring_set.add(s[right])
            # check if current substring length is greater or not
            result = max(result, right-left+1)
        
        return result