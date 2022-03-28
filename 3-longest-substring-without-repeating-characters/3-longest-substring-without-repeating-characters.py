class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # O(N) space and time
        
        seen = ''
        max_len = 0
        
        for ch in s:
            # ch not in the seen add it to it
            if ch not in seen:
                seen+=ch
            
            else:
                # if ch is in seen we need to move past it
                # that is we take seen after the first occurence of ch and then append the newely appeared
                # character to it 
                seen = seen[seen.index(ch)+1:]+ch
            
            max_len=max(max_len,len(seen))
        
        return max_len
                