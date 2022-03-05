class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        last = s.split(" ")
        
        for idx in range(len(last)-1,-1,-1):
            if len(last[idx]) == 0:
                continue
                
            else:
                return len(last[idx])
        