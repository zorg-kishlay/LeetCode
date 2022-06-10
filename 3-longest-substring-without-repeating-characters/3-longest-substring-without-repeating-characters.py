class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = ''
        max_len = 0
        for ch in s:
            
            if ch not in seen:
                seen+=ch
            
            else:
                seen = seen[seen.index(ch)+1:]+ch
            
            max_len = max(max_len,len(seen))
        
        
        return max_len
            
        